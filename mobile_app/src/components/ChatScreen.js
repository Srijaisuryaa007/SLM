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
      text: "Hi! I'm your English Class 9 Textbook Assistant. Ask me any question from your lessons (such as 'Learning the Game', 'I Can't Climb Trees Anymore', 'Seventeen Oranges', or 'Water – The Elixir of Life')!",
      fact: null,
    },
  ]);
  const [input, setInput] = useState('');
  const [statusText, setStatusText] = useState('Initializing English AI...');
  const [isModelReady, setIsModelReady] = useState(false);
  const [loading, setLoading] = useState(false);
  const llamaContext = useRef(null);
  const flatListRef = useRef(null);

  useEffect(() => {
    let isMounted = true;

    // Delay model initialization slightly so UI renders smoothly first
    const timer = setTimeout(async () => {
      try {
        if (!isMounted) return;
        setStatusText('Loading Qwen 0.5B model...');

        let ctx = null;
        const candidates = Platform.OS === 'android'
          ? ['/data/user/0/com.brightpathapp/files/model.gguf', '/data/data/com.brightpathapp/files/model.gguf', 'model.gguf']
          : ['model.gguf'];

        let lastErr = null;
        for (const candidate of candidates) {
          try {
            ctx = await initLlama(
              {
                model: candidate,
                is_model_asset: candidate === 'model.gguf',
                n_ctx: 512,
                n_threads: 2,
                n_gpu_layers: 0,
                use_mlock: false,
              },
              (progress) => {
                if (isMounted) {
                  const pct = Math.round(progress * 100);
                  setStatusText(`Loading Model: ${pct}%`);
                }
              }
            );
            if (ctx) break;
          } catch (e) {
            lastErr = e;
          }
        }

        if (!ctx && lastErr) throw lastErr;

        if (isMounted) {
          llamaContext.current = ctx;
          setIsModelReady(true);
          setStatusText('Offline English AI Ready (Qwen 0.5B)');
        }
      } catch (err) {
        console.warn('Llama init notice:', err);
        if (isMounted) {
          // If native SLM context is still copying/extracting, set offline Q&A mode
          setStatusText('Offline English Assistant Ready');
          setIsModelReady(true);
        }
      }
    }, 500);

    return () => {
      isMounted = false;
      clearTimeout(timer);
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

    const botMsgId = (Date.now() + 1).toString();

    // 1. SEARCH TEXTBOOK (Comprehension Q&A Bank or Clean Story Prose)
    const ragResult = findFact(questionText);

    // Case A: High-precision textbook comprehension question direct hit
    if (ragResult && ragResult.isDirectQA) {
      const botMsg = {
        id: botMsgId,
        role: 'assistant',
        text: ragResult.answer,
        fact: `Book Page ${ragResult.page}: "${ragResult.evidence}"`,
      };
      setMessages((prev) => [...prev, botMsg]);
      setLoading(false);
      return;
    }

    // Case B: Freeform question - Search story excerpt & feed to on-device SLM
    const excerpt = ragResult ? ragResult.chunk : null;
    const pageNo = ragResult ? ragResult.page : null;
    const citation = excerpt
      ? `Book Page ${pageNo}: "${excerpt.slice(0, 180)}..."`
      : null;

    const prompt = buildChatML(questionText, excerpt, pageNo);

    const initialBotMsg = {
      id: botMsgId,
      role: 'assistant',
      text: '',
      fact: citation,
    };
    setMessages((prev) => [...prev, initialBotMsg]);

    try {
      if (llamaContext.current) {
        let accumulated = '';
        await llamaContext.current.completion(
          {
            prompt: prompt,
            n_predict: 120,
            temperature: 0.0, // Strict zero-hallucination
            stop: ['<|im_end|>', '<|endoftext|>', '<|im_start|>'],
          },
          (tokenData) => {
            accumulated += tokenData.token;
            setMessages((prev) =>
              prev.map((msg) =>
                msg.id === botMsgId ? { ...msg, text: accumulated.trim() } : msg
              )
            );
          }
        );
      } else {
        // Direct answer if native model is still loading
        const fallbackText = excerpt
          ? `From Book Page ${pageNo}: ${excerpt}`
          : "Not mentioned in the English Class 9 textbook.";
        setMessages((prev) =>
          prev.map((msg) =>
            msg.id === botMsgId ? { ...msg, text: fallbackText } : msg
          )
        );
      }
    } catch (e) {
      console.warn('Inference notice:', e);
      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === botMsgId
            ? {
                ...msg,
                text: excerpt
                  ? `From Book Page ${pageNo}: ${excerpt}`
                  : "Not mentioned in the book.",
              }
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
          <Text style={styles.title}>English Class 9 AI Assistant</Text>
          <Text style={styles.subtitle}>{statusText}</Text>
        </View>
        <View style={[styles.badge, isModelReady ? styles.badgeReady : styles.badgeLoading]}>
          <Text style={styles.badgeText}>{isModelReady ? 'Offline' : 'Loading'}</Text>
        </View>
      </View>

      {/* Suggested Quick Questions from Textbook */}
      <View style={styles.suggestions}>
        <TouchableOpacity
          style={styles.chip}
          onPress={() => handleSend("What did the visitor hide in the jackfruit tree?")}
        >
          <Text style={styles.chipText}>Jackfruit tree treasure?</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.chip}
          onPress={() => handleSend("Who was Sachin's coach?")}
        >
          <Text style={styles.chipText}>Sachin's coach?</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.chip}
          onPress={() => handleSend("What was the narrator carrying in Seventeen Oranges?")}
        >
          <Text style={styles.chipText}>Seventeen Oranges?</Text>
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

            {/* Verified Textbook Citation Card */}
            {item.fact && (
              <View style={styles.factCard}>
                <Text style={styles.factLabel}>Textbook Citation:</Text>
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
            placeholder="Ask a question from Class 9 English..."
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
    fontSize: 17,
    fontWeight: '700',
    color: '#1C1C1E',
  },
  subtitle: {
    fontSize: 12,
    color: '#6B7280',
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
    backgroundColor: '#EEF2FF',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#E0E7FF',
  },
  chipText: {
    fontSize: 12,
    color: '#3730A3',
    fontWeight: '500',
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
