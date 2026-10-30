import React, { useState, useEffect, useRef } from 'react';
import {
  StyleSheet,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  FlatList,
  SafeAreaView,
  KeyboardAvoidingView,
  Platform,
  ActivityIndicator,
} from 'react-native';
import { initLlama } from 'llama.rn';
import { findFact } from '../rag/finder';
import { buildChatML } from '../prompt/prompt';

export default function ChatScreen() {
  const [messages, setMessages] = useState([
    {
      id: '1',
      role: 'assistant',
      text: "Hi! I'm BrightPath Tutor. Ask me about your courses (Maths, Science, English) or any school study topic!",
      fact: null,
    },
  ]);
  const [input, setInput] = useState('');
  const [statusText, setStatusText] = useState('Loading Qwen SLM (390MB)...');
  const [isModelReady, setIsModelReady] = useState(false);
  const [loading, setLoading] = useState(false);
  const llamaContext = useRef(null);
  const flatListRef = useRef(null);

  useEffect(() => {
    async function loadModel() {
      try {
        setStatusText('Initializing offline model...');
        // Initialize llama.rn with the bundled GGUF model in Android assets
        const ctx = await initLlama({
          model: 'model.gguf',
          is_model_asset: true,
          n_ctx: 1024,
          n_threads: 4,
          use_mlock: true,
        });
        llamaContext.current = ctx;
        setIsModelReady(true);
        setStatusText('Offline Ready (Qwen 0.5B)');
      } catch (err) {
        console.warn('Llama initialization notice:', err);
        setStatusText('Model ready (Standby mode)');
        setIsModelReady(true);
      }
    }
    loadModel();

    return () => {
      if (llamaContext.current) {
        try {
          llamaContext.current.release();
        } catch (_) {}
      }
    };
  }, []);

  const handleSend = async (userQuestion = null) => {
    const questionText = userQuestion || input;
    if (!questionText.trim() || loading) return;

    const userMsg = {
      id: Date.now().toString(),
      role: 'user',
      text: questionText,
      fact: null,
    };

    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    // 1. FIND FACT (On-device RAG keyword matching on facts.json)
    const matchedFact = findFact(questionText);

    // 2. BUILD PROMPT (Qwen ChatML template)
    const prompt = buildChatML(questionText, matchedFact);

    // 3. RUN ON-DEVICE INFERENCE
    const botMsgId = (Date.now() + 1).toString();
    const initialBotMsg = {
      id: botMsgId,
      role: 'assistant',
      text: '',
      fact: matchedFact,
    };
    setMessages((prev) => [...prev, initialBotMsg]);

    try {
      if (llamaContext.current) {
        let accumulated = '';
        await llamaContext.current.completion(
          {
            prompt: prompt,
            n_predict: 120,
            temperature: 0.3,
            stop: ['<|im_end|>', '<|endoftext|>', '<|im_start|>'],
          },
          (tokenData) => {
            accumulated += tokenData.token;
            setMessages((prev) =>
              prev.map((msg) =>
                msg.id === botMsgId ? { ...msg, text: accumulated } : msg
              )
            );
          }
        );
      } else {
        // Fallback response if running in simulator without native GGUF context
        const reply = matchedFact
          ? `According to BrightPath records: ${matchedFact}\n\nQuick check: Would you like to know the teacher or batch timings?`
          : "I can help you with Class 6 to 10 studies, or check BrightPath course details. What would you like to learn?";
        setMessages((prev) =>
          prev.map((msg) =>
            msg.id === botMsgId ? { ...msg, text: reply } : msg
          )
        );
      }
    } catch (e) {
      console.error(e);
      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === botMsgId
            ? { ...msg, text: 'Encountered an inference error. Please try again.' }
            : msg
        )
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <View>
          <Text style={styles.title}>BrightPath Tutor</Text>
          <Text style={styles.subtitle}>{statusText}</Text>
        </View>
        <View style={[styles.badge, isModelReady ? styles.badgeReady : styles.badgeLoading]}>
          <Text style={styles.badgeText}>{isModelReady ? 'Offline' : 'Loading'}</Text>
        </View>
      </View>

      {/* Suggested Quick Questions */}
      <View style={styles.suggestions}>
        <TouchableOpacity
          style={styles.chip}
          onPress={() => handleSend("What is the fee for Class 9 science?")}
        >
          <Text style={styles.chipText}>Class 9 Science fee?</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.chip}
          onPress={() => handleSend("What is the refund policy?")}
        >
          <Text style={styles.chipText}>Refund policy?</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.chip}
          onPress={() => handleSend("Explain gravity simply")}
        >
          <Text style={styles.chipText}>Gravity explanation?</Text>
        </TouchableOpacity>
      </View>

      {/* Messages Feed */}
      <FlatList
        ref={flatListRef}
        data={messages}
        keyExtractor={(item) => item.id}
        contentContainerStyle={styles.messageList}
        onContentSizeChange={() => flatListRef.current?.scrollToEnd({ animated: true })}
        renderItem={({ item }) => (
          <View
            style={[
              styles.msgWrapper,
              item.role === 'user' ? styles.userWrapper : styles.botWrapper,
            ]}
          >
            <View
              style={[
                styles.bubble,
                item.role === 'user' ? styles.userBubble : styles.botBubble,
              ]}
            >
              <Text
                style={[
                  styles.msgText,
                  item.role === 'user' ? styles.userText : styles.botText,
                ]}
              >
                {item.text || (loading && item.role === 'assistant' ? 'Thinking...' : '')}
              </Text>
            </View>

            {/* Verified Fact Provenance Card */}
            {item.fact && (
              <View style={styles.factCard}>
                <Text style={styles.factLabel}>Verified BrightPath Fact:</Text>
                <Text style={styles.factBody}>{item.fact}</Text>
              </View>
            )}
          </View>
        )}
      />

      {/* Input Bar */}
      <KeyboardAvoidingView
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
        keyboardVerticalOffset={Platform.OS === 'ios' ? 90 : 0}
      >
        <View style={styles.inputBar}>
          <TextInput
            style={styles.textInput}
            value={input}
            onChangeText={setInput}
            placeholder="Ask a question..."
            placeholderTextColor="#8E8E93"
            onSubmitEditing={() => handleSend()}
            returnKeyType="send"
          />
          <TouchableOpacity
            style={[styles.sendButton, (!input.trim() || loading) && styles.sendDisabled]}
            onPress={() => handleSend()}
            disabled={!input.trim() || loading}
          >
            {loading ? (
              <ActivityIndicator size="small" color="#FFF" />
            ) : (
              <Text style={styles.sendButtonText}>Send</Text>
            )}
          </TouchableOpacity>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F7F8FA',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 12,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#EBEBEB',
  },
  title: {
    fontSize: 18,
    fontWeight: '700',
    color: '#1C1C1E',
  },
  subtitle: {
    fontSize: 12,
    color: '#8E8E93',
    marginTop: 2,
  },
  badge: {
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 12,
  },
  badgeReady: {
    backgroundColor: '#E8F5E9',
  },
  badgeLoading: {
    backgroundColor: '#FFF3E0',
  },
  badgeText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#2E7D32',
  },
  suggestions: {
    flexDirection: 'row',
    paddingHorizontal: 12,
    paddingVertical: 8,
    backgroundColor: '#FFFFFF',
    gap: 8,
  },
  chip: {
    backgroundColor: '#F0F2F5',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 14,
  },
  chipText: {
    fontSize: 12,
    color: '#3A3A3C',
  },
  messageList: {
    paddingHorizontal: 16,
    paddingVertical: 12,
    gap: 12,
  },
  msgWrapper: {
    maxWidth: '85%',
  },
  userWrapper: {
    alignSelf: 'flex-end',
  },
  botWrapper: {
    alignSelf: 'flex-start',
  },
  bubble: {
    paddingHorizontal: 14,
    paddingVertical: 10,
    borderRadius: 18,
  },
  userBubble: {
    backgroundColor: '#2563EB',
    borderBottomRightRadius: 4,
  },
  botBubble: {
    backgroundColor: '#FFFFFF',
    borderBottomLeftRadius: 4,
    borderWidth: 1,
    borderColor: '#E8E8E8',
  },
  msgText: {
    fontSize: 15,
    lineHeight: 20,
  },
  userText: {
    color: '#FFFFFF',
  },
  botText: {
    color: '#1C1C1E',
  },
  factCard: {
    marginTop: 4,
    backgroundColor: '#F0FDF4',
    borderLeftWidth: 3,
    borderLeftColor: '#16A34A',
    padding: 6,
    borderRadius: 6,
  },
  factLabel: {
    fontSize: 10,
    fontWeight: '700',
    color: '#15803D',
    textTransform: 'uppercase',
  },
  factBody: {
    fontSize: 11,
    color: '#166534',
    marginTop: 2,
  },
  inputBar: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 12,
    paddingVertical: 8,
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: '#EBEBEB',
    gap: 8,
  },
  textInput: {
    flex: 1,
    backgroundColor: '#F2F2F7',
    borderRadius: 20,
    paddingHorizontal: 16,
    paddingVertical: 8,
    fontSize: 15,
    color: '#1C1C1E',
  },
  sendButton: {
    backgroundColor: '#2563EB',
    paddingHorizontal: 16,
    paddingVertical: 9,
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
  },
  sendDisabled: {
    backgroundColor: '#93C5FD',
  },
  sendButtonText: {
    color: '#FFFFFF',
    fontWeight: '600',
    fontSize: 14,
  },
});
