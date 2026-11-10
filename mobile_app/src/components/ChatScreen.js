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
  ScrollView,
} from 'react-native';
import { initLlama } from 'llama.rn';
import { findFact } from '../rag/finder';
import { buildChatML } from '../prompt/prompt';

/**
 * Helper to render text with **bold** or [bracketed] highlighted words.
 */
function HighlightedText({ text, baseStyle, highlightStyle }) {
  if (!text) return null;
  const parts = text.split(/(\*\*.*?\*\*|\[.*?\])/g);
  return (
    <Text style={baseStyle}>
      {parts.map((part, index) => {
        if (
          (part.startsWith('**') && part.endsWith('**')) ||
          (part.startsWith('[') && part.endsWith(']'))
        ) {
          const clean = part.replace(/^\*\*|^\/|^\*|^\/|^\s+|\s+$|\*\*$/g, '').replace(/^\[|\]$/g, '');
          return (
            <Text key={index} style={[styles.inlineHighlight, highlightStyle]}>
              {` ${clean} `}
            </Text>
          );
        }
        return part;
      })}
    </Text>
  );
}

/**
 * Educational Answer Card: Prominently highlights answers, fill-in-the-blanks,
 * match-the-following pairs, and textbook page proofs.
 */
function AnswerCard({ item, loading }) {
  const structured = item.structured;

  // 1. Structured Comprehension or Exercise Match
  if (structured) {
    return (
      <View style={styles.educationalCard}>
        {/* Direct Answer Banner */}
        {structured.direct_answer ? (
          <View style={styles.directAnswerBox}>
            <View style={styles.badgeRow}>
              <View style={styles.answerTag}>
                <Text style={styles.answerTagText}>🎯 DIRECT ANSWER</Text>
              </View>
            </View>
            <Text style={styles.directAnswerText}>{structured.direct_answer}</Text>
          </View>
        ) : null}

        {/* Fill in the Blanks / Completed Sentence */}
        {structured.completed_sentence ? (
          <View style={styles.sentenceBox}>
            <Text style={styles.sectionHeading}>📝 COMPLETED SENTENCE:</Text>
            <HighlightedText
              text={structured.completed_sentence}
              baseStyle={styles.sentenceText}
              highlightStyle={styles.blankHighlight}
            />
          </View>
        ) : null}

        {/* Match the Following Exercise Table */}
        {structured.matches && structured.matches.length > 0 ? (
          <View style={styles.matchesBox}>
            <Text style={styles.sectionHeading}>📋 MATCH THE FOLLOWING:</Text>
            <View style={styles.tableContainer}>
              {structured.matches.map(([left, right], idx) => (
                <View
                  key={idx}
                  style={[
                    styles.matchRow,
                    idx % 2 === 1 && styles.matchRowAlt,
                  ]}
                >
                  <Text style={styles.matchLeft}>{left}</Text>
                  <Text style={styles.matchArrow}>➔</Text>
                  <Text style={styles.matchRight}>{right}</Text>
                </View>
              ))}
            </View>
          </View>
        ) : null}

        {/* Brief Explanation / Context */}
        {structured.explanation ? (
          <View style={styles.explanationBox}>
            <Text style={styles.explanationText}>
              💡 <Text style={styles.boldLabel}>Note:</Text> {structured.explanation}
            </Text>
          </View>
        ) : null}

        {/* Textbook Proof & Citation */}
        {structured.page && (
          <View style={styles.proofCard}>
            <View style={styles.proofHeader}>
              <Text style={styles.proofTitle}>📖 VERIFIED TEXTBOOK PROOF</Text>
              <View style={styles.pagePill}>
                <Text style={styles.pagePillText}>Book Page {structured.page}</Text>
              </View>
            </View>
            {structured.evidence ? (
              <Text style={styles.proofQuote}>"{structured.evidence}"</Text>
            ) : null}
          </View>
        )}
      </View>
    );
  }

  // 2. Freeform Response (from on-device neural SLM)
  return (
    <View style={styles.freeformCard}>
      {item.text ? (
        <HighlightedText
          text={item.text}
          baseStyle={styles.botText}
          highlightStyle={styles.inlineHighlight}
        />
      ) : loading ? (
        <View style={styles.loadingRow}>
          <ActivityIndicator size="small" color="#2563EB" />
          <Text style={styles.loadingText}>Reading textbook...</Text>
        </View>
      ) : null}

      {/* Citation if present */}
      {item.fact && (
        <View style={styles.proofCard}>
          <View style={styles.proofHeader}>
            <Text style={styles.proofTitle}>📖 TEXTBOOK CITATION</Text>
          </View>
          <Text style={styles.proofQuote}>{item.fact}</Text>
        </View>
      )}
    </View>
  );
}

export default function ChatScreen() {
  const [messages, setMessages] = useState([
    {
      id: '1',
      role: 'assistant',
      text: null,
      structured: {
        direct_answer: 'Tamil Nadu English Class 9 AI Assistant Ready',
        explanation:
          'Ask any question, fill in the blank, or match-the-following from your textbook (e.g., Learning the Game, I Can’t Climb Trees Anymore, Seventeen Oranges, Water – The Elixir of Life)!',
        page: '1 - 122',
        evidence: 'Grounded strictly on TN English Class 9 Textbook with Zero Hallucination.',
      },
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

    const timer = setTimeout(async () => {
      try {
        if (!isMounted) return;
        setStatusText('Loading Qwen 0.5B model...');

        let ctx = null;
        const candidates =
          Platform.OS === 'android'
            ? [
                '/data/user/0/com.brightpathapp/files/model.gguf',
                '/data/data/com.brightpathapp/files/model.gguf',
                'model.gguf',
              ]
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
          setStatusText('Offline English Assistant Ready');
          setIsModelReady(true);
        }
      }
    }, 400);

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
    };

    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    const botMsgId = (Date.now() + 1).toString();

    // 1. SEARCH TEXTBOOK (High precision Q&A Bank or Clean Story Prose)
    const ragResult = findFact(questionText);

    // Case A: High-precision textbook exercise or direct hit
    if (ragResult && ragResult.isDirectQA) {
      const botMsg = {
        id: botMsgId,
        role: 'assistant',
        text: ragResult.answer,
        structured: ragResult.structured,
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
      ? `Book Page ${pageNo}: "${excerpt.slice(0, 160)}..."`
      : null;

    const prompt = buildChatML(questionText, excerpt, pageNo);

    const initialBotMsg = {
      id: botMsgId,
      role: 'assistant',
      text: '',
      structured: null,
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
        const fallbackText = excerpt
          ? `From Book Page ${pageNo}: ${excerpt}`
          : 'Not mentioned in the English Class 9 textbook.';
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
                  : 'Not mentioned in the book.',
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
        <View style={styles.headerTitles}>
          <Text style={styles.title}>English Class 9 AI</Text>
          <Text style={styles.subtitle}>{statusText}</Text>
        </View>
        <View
          style={[
            styles.badge,
            isModelReady ? styles.badgeReady : styles.badgeLoading,
          ]}
        >
          <Text style={styles.badgeText}>
            {isModelReady ? 'Offline Ready' : 'Loading'}
          </Text>
        </View>
      </View>

      {/* Suggested Quick Questions & Exercise Chips */}
      <View style={styles.chipContainer}>
        <ScrollView
          horizontal
          showsHorizontalScrollIndicator={false}
          contentContainerStyle={styles.chipScroll}
        >
          <TouchableOpacity
            style={styles.chip}
            onPress={() =>
              handleSend('The visitor gifted the _________ to the little girl.')
            }
          >
            <Text style={styles.chipText}>🎯 Fill: Visitor's Gift?</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.chip}
            onPress={() =>
              handleSend('Match the following: pruning, chiming, drenched')
            }
          >
            <Text style={styles.chipText}>📋 Match: Unit 2 Words</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.chip}
            onPress={() => handleSend("Who was Sachin's coach?")}
          >
            <Text style={styles.chipText}>🏏 Sachin's Coach?</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.chip}
            onPress={() =>
              handleSend('What did the visitor hide in the jackfruit tree?')
            }
          >
            <Text style={styles.chipText}>🌳 Jackfruit Tree Treasure?</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.chip}
            onPress={() =>
              handleSend('What is the real elixir of life according to Sir C.V. Raman?')
            }
          >
            <Text style={styles.chipText}>💧 Real Elixir of Life?</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.chip}
            onPress={() =>
              handleSend('Where did the narrator work in Seventeen Oranges?')
            }
          >
            <Text style={styles.chipText}>🍊 Seventeen Oranges Job?</Text>
          </TouchableOpacity>
        </ScrollView>
      </View>

      {/* Messages Feed */}
      <FlatList
        ref={flatListRef}
        data={messages}
        keyExtractor={(item) => item.id}
        contentContainerStyle={styles.messageList}
        onContentSizeChange={() =>
          flatListRef.current?.scrollToEnd({ animated: true })
        }
        renderItem={({ item }) => (
          <View
            style={[
              styles.msgWrapper,
              item.role === 'user' ? styles.userWrapper : styles.botWrapper,
            ]}
          >
            {item.role === 'user' ? (
              <View style={styles.userBubble}>
                <Text style={styles.userText}>{item.text}</Text>
              </View>
            ) : (
              <AnswerCard item={item} loading={loading} />
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
            placeholder="Ask question, fill in blank, or match..."
            placeholderTextColor="#94A3B8"
            onSubmitEditing={() => handleSend()}
            returnKeyType="send"
          />
          <TouchableOpacity
            style={[
              styles.sendButton,
              (!input.trim() || loading) && styles.sendDisabled,
            ]}
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
    backgroundColor: '#F1F5F9',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 12,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
    elevation: 2,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowOffset: { width: 0, height: 1 },
    shadowRadius: 3,
  },
  headerTitles: {
    flex: 1,
  },
  title: {
    fontSize: 18,
    fontWeight: '800',
    color: '#0F172A',
  },
  subtitle: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 2,
  },
  badge: {
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 14,
  },
  badgeReady: {
    backgroundColor: '#DCFCE7',
  },
  badgeLoading: {
    backgroundColor: '#FEF3C7',
  },
  badgeText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#15803D',
  },
  chipContainer: {
    backgroundColor: '#FFFFFF',
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
  },
  chipScroll: {
    paddingHorizontal: 12,
  },
  chip: {
    backgroundColor: '#EFF6FF',
    borderColor: '#BFDBFE',
    borderWidth: 1,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
    marginRight: 8,
  },
  chipText: {
    fontSize: 12.5,
    fontWeight: '600',
    color: '#1D4ED8',
  },
  messageList: {
    paddingHorizontal: 14,
    paddingVertical: 12,
  },
  msgWrapper: {
    marginVertical: 6,
    maxWidth: '92%',
  },
  userWrapper: {
    alignSelf: 'flex-end',
  },
  botWrapper: {
    alignSelf: 'flex-start',
    width: '100%',
  },
  userBubble: {
    backgroundColor: '#2563EB',
    paddingHorizontal: 16,
    paddingVertical: 11,
    borderRadius: 18,
    borderBottomRightRadius: 4,
    elevation: 1,
  },
  userText: {
    fontSize: 15,
    color: '#FFFFFF',
    lineHeight: 21,
    fontWeight: '500',
  },
  educationalCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    elevation: 2,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
  },
  freeformCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    elevation: 2,
  },
  directAnswerBox: {
    backgroundColor: '#ECFDF5',
    borderLeftWidth: 4,
    borderLeftColor: '#10B981',
    borderRadius: 10,
    padding: 12,
    marginBottom: 10,
  },
  badgeRow: {
    flexDirection: 'row',
    marginBottom: 4,
  },
  answerTag: {
    backgroundColor: '#D1FAE5',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 6,
  },
  answerTagText: {
    fontSize: 11,
    fontWeight: '800',
    color: '#065F46',
    letterSpacing: 0.5,
  },
  directAnswerText: {
    fontSize: 17,
    fontWeight: '800',
    color: '#064E3B',
    lineHeight: 23,
    marginTop: 2,
  },
  sentenceBox: {
    backgroundColor: '#F8FAFC',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 12,
    marginBottom: 10,
  },
  sectionHeading: {
    fontSize: 11.5,
    fontWeight: '800',
    color: '#475569',
    marginBottom: 6,
    letterSpacing: 0.5,
  },
  sentenceText: {
    fontSize: 14.5,
    color: '#1E293B',
    lineHeight: 22,
  },
  blankHighlight: {
    backgroundColor: '#FEF08A',
    color: '#854D0E',
    fontWeight: '800',
    borderRadius: 4,
  },
  inlineHighlight: {
    backgroundColor: '#FEF08A',
    color: '#854D0E',
    fontWeight: '700',
  },
  matchesBox: {
    backgroundColor: '#F8FAFC',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 12,
    marginBottom: 10,
  },
  tableContainer: {
    borderRadius: 8,
    overflow: 'hidden',
    borderWidth: 1,
    borderColor: '#CBD5E1',
  },
  matchRow: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 8,
    paddingHorizontal: 10,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#F1F5F9',
  },
  matchRowAlt: {
    backgroundColor: '#F8FAFC',
  },
  matchLeft: {
    flex: 1,
    fontSize: 13.5,
    fontWeight: '700',
    color: '#1E293B',
  },
  matchArrow: {
    fontSize: 14,
    fontWeight: '800',
    color: '#2563EB',
    paddingHorizontal: 8,
  },
  matchRight: {
    flex: 1.3,
    fontSize: 13.5,
    fontWeight: '600',
    color: '#047857',
  },
  explanationBox: {
    paddingVertical: 4,
    marginBottom: 8,
  },
  explanationText: {
    fontSize: 13,
    color: '#475569',
    lineHeight: 18,
  },
  boldLabel: {
    fontWeight: '700',
    color: '#334155',
  },
  proofCard: {
    backgroundColor: '#F1F5F9',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#CBD5E1',
    padding: 10,
    marginTop: 4,
  },
  proofHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 6,
  },
  proofTitle: {
    fontSize: 11,
    fontWeight: '800',
    color: '#334155',
    letterSpacing: 0.5,
  },
  pagePill: {
    backgroundColor: '#DBEAFE',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 10,
  },
  pagePillText: {
    fontSize: 11,
    fontWeight: '800',
    color: '#1D4ED8',
  },
  proofQuote: {
    fontSize: 12.5,
    fontStyle: 'italic',
    color: '#475569',
    lineHeight: 18,
  },
  botText: {
    fontSize: 14.5,
    color: '#1E293B',
    lineHeight: 22,
  },
  loadingRow: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 6,
  },
  loadingText: {
    fontSize: 13,
    color: '#64748B',
    marginLeft: 8,
  },
  inputBar: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 12,
    paddingVertical: 8,
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: '#E2E8F0',
  },
  textInput: {
    flex: 1,
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 22,
    paddingHorizontal: 16,
    paddingVertical: 10,
    fontSize: 14,
    color: '#0F172A',
    maxHeight: 100,
  },
  sendButton: {
    backgroundColor: '#2563EB',
    paddingHorizontal: 16,
    paddingVertical: 11,
    borderRadius: 22,
    marginLeft: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },
  sendDisabled: {
    backgroundColor: '#94A3B8',
  },
  sendButtonText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '700',
  },
});
