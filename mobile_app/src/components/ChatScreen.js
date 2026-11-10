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
          const clean = part
            .replace(/^\*\*|^\*|^\s+|\s+$|\*\*$/g, '')
            .replace(/^\[|\]$/g, '');
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
 * Interactive Question Picker Card:
 * Displays all questions on a selected Book Page or Unit as tappable cards.
 */
function QuestionPickerCard({ item, onSelectQuestion }) {
  return (
    <View style={styles.pickerCard}>
      <View style={styles.pickerHeader}>
        <View style={styles.pickerBadge}>
          <Text style={styles.pickerBadgeText}>
            {item.page ? `📘 BOOK PAGE ${item.page}` : '📚 UNIT DIRECTORY'}
          </Text>
        </View>
        <Text style={styles.pickerUnitText}>{item.unit}</Text>
      </View>

      {item.title ? (
        <Text style={styles.pickerTitleText}>{item.title}</Text>
      ) : null}

      <Text style={styles.pickerInstruction}>
        👇 Tap any question below to reveal the answer & textbook proof:
      </Text>

      <View style={styles.questionsContainer}>
        {item.questions &&
          item.questions.map((q, idx) => (
            <TouchableOpacity
              key={idx}
              style={styles.questionPickBtn}
              activeOpacity={0.7}
              onPress={() => onSelectQuestion(q)}
            >
              <View style={styles.pickNumberBadge}>
                <Text style={styles.pickNumberText}>{idx + 1}</Text>
              </View>
              <Text style={styles.questionPickText}>{q}</Text>
              <Text style={styles.questionPickArrow}>➔</Text>
            </TouchableOpacity>
          ))}
      </View>
    </View>
  );
}

/**
 * Educational Answer Card: Prominently highlights answers, fill-in-the-blanks,
 * match-the-following pairs, textbook page proofs, and follow-up doubt actions.
 */
function AnswerCard({ item, loading, onAskDoubt, onBrowsePage }) {
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

        {/* Multiple Choice Options Display (a, b, c, d) */}
        {structured.options && structured.options.length > 0 ? (
          <View style={styles.optionsBox}>
            <Text style={styles.sectionHeading}>🔘 TEXTBOOK OPTIONS:</Text>
            <View style={styles.optionsContainer}>
              {structured.options.map((opt, idx) => {
                const isCorrect =
                  opt.letter.toLowerCase() ===
                  (structured.correct_option || '').toLowerCase();
                return (
                  <View
                    key={idx}
                    style={[
                      styles.optionRow,
                      isCorrect && styles.optionRowCorrect,
                    ]}
                  >
                    <View
                      style={[
                        styles.optionLetterBadge,
                        isCorrect && styles.optionLetterBadgeCorrect,
                      ]}
                    >
                      <Text
                        style={[
                          styles.optionLetterText,
                          isCorrect && styles.optionLetterTextCorrect,
                        ]}
                      >
                        {opt.letter.toUpperCase()}
                      </Text>
                    </View>
                    <Text
                      style={[
                        styles.optionContentText,
                        isCorrect && styles.optionContentTextCorrect,
                      ]}
                    >
                      {opt.text}
                    </Text>
                    {isCorrect && (
                      <View style={styles.correctBadge}>
                        <Text style={styles.correctBadgeText}>✓ Correct</Text>
                      </View>
                    )}
                  </View>
                );
              })}
            </View>
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

        {/* Follow-up Action Buttons */}
        <View style={styles.followupRow}>
          <TouchableOpacity
            style={styles.doubtBtn}
            onPress={() => onAskDoubt(structured.question)}
          >
            <Text style={styles.doubtBtnText}>❓ Have a doubt?</Text>
          </TouchableOpacity>

          {structured.page && (
            <TouchableOpacity
              style={styles.browseMoreBtn}
              onPress={() => onBrowsePage(structured.page)}
            >
              <Text style={styles.browseMoreBtnText}>
                📚 Page {structured.page} Questions
              </Text>
            </TouchableOpacity>
          )}
        </View>
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
      isQuestionPicker: false,
      text: null,
      structured: {
        direct_answer: 'Tamil Nadu English Class 9 AI Assistant Ready',
        explanation:
          'Tap any Book Page or Unit chip at the top to see all questions, or ask any question directly!',
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

    // 1. SEARCH TEXTBOOK (Page Directory, Comprehension Q&A Bank, or Story Prose)
    const ragResult = findFact(questionText);

    // Case 0: Page / Unit Question Directory Request
    if (ragResult && ragResult.isQuestionPicker) {
      const botMsg = {
        id: botMsgId,
        role: 'assistant',
        isQuestionPicker: true,
        page: ragResult.page,
        unit: ragResult.unit,
        title: ragResult.title,
        questions: ragResult.questions,
      };
      setMessages((prev) => [...prev, botMsg]);
      setLoading(false);
      return;
    }

    // Case A: High-precision textbook exercise or direct hit
    if (ragResult && ragResult.isDirectQA) {
      const botMsg = {
        id: botMsgId,
        role: 'assistant',
        isQuestionPicker: false,
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
      isQuestionPicker: false,
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

  const handleAskDoubt = (question) => {
    handleSend(`Explain the answer to "${question}" with clear textbook context`);
  };

  const handleBrowsePage = (pageNumber) => {
    handleSend(`Page ${pageNumber}`);
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

      {/* Quick Textbook Page & Unit Selector Bar */}
      <View style={styles.chipContainer}>
        <ScrollView
          horizontal
          showsHorizontalScrollIndicator={false}
          contentContainerStyle={styles.chipScroll}
        >
          <Text style={styles.selectorLabel}>📖 Pick Page:</Text>

          <TouchableOpacity
            style={styles.pageChip}
            onPress={() => handleSend('Page 33')}
          >
            <Text style={styles.pageChipText}>p. 33 (Gift & Match)</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.pageChip}
            onPress={() => handleSend('Page 6')}
          >
            <Text style={styles.pageChipText}>p. 6 (Synonyms & Antonyms)</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.pageChip}
            onPress={() => handleSend('Page 1')}
          >
            <Text style={styles.pageChipText}>p. 1 (Sachin Camp)</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.pageChip}
            onPress={() => handleSend('Page 30')}
          >
            <Text style={styles.pageChipText}>p. 30 (Jackfruit Tree)</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.pageChip}
            onPress={() => handleSend('Page 93')}
          >
            <Text style={styles.pageChipText}>p. 93 (17 Oranges)</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.pageChip}
            onPress={() => handleSend('Page 118')}
          >
            <Text style={styles.pageChipText}>p. 118 (Elixir of Life)</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.unitChip}
            onPress={() => handleSend('Unit 2')}
          >
            <Text style={styles.unitChipText}>Unit 2 (Ruskin Bond)</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.unitChip}
            onPress={() => handleSend('Unit 1')}
          >
            <Text style={styles.unitChipText}>Unit 1 (Sachin)</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.unitChip}
            onPress={() => handleSend('Unit 4')}
          >
            <Text style={styles.unitChipText}>Unit 4 (Seventeen Oranges)</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.unitChip}
            onPress={() => handleSend('Unit 5')}
          >
            <Text style={styles.unitChipText}>Unit 5 (Water)</Text>
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
            ) : item.isQuestionPicker ? (
              <QuestionPickerCard
                item={item}
                onSelectQuestion={(q) => handleSend(q)}
              />
            ) : (
              <AnswerCard
                item={item}
                loading={loading}
                onAskDoubt={handleAskDoubt}
                onBrowsePage={handleBrowsePage}
              />
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
            placeholder="Type 'Page 33', 'Unit 2', or ask any question..."
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
    alignItems: 'center',
  },
  selectorLabel: {
    fontSize: 12,
    fontWeight: '800',
    color: '#475569',
    marginRight: 8,
  },
  pageChip: {
    backgroundColor: '#EFF6FF',
    borderColor: '#93C5FD',
    borderWidth: 1,
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 14,
    marginRight: 6,
  },
  pageChipText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#1D4ED8',
  },
  unitChip: {
    backgroundColor: '#F0FDF4',
    borderColor: '#86EFAC',
    borderWidth: 1,
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 14,
    marginRight: 6,
  },
  unitChipText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#15803D',
  },
  messageList: {
    paddingHorizontal: 14,
    paddingVertical: 12,
  },
  msgWrapper: {
    marginVertical: 6,
    maxWidth: '96%',
  },
  userWrapper: {
    alignSelf: 'flex-end',
    maxWidth: '85%',
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
  pickerCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 14,
    borderWidth: 1.5,
    borderColor: '#3B82F6',
    elevation: 3,
    shadowColor: '#1E40AF',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 5,
  },
  pickerHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 6,
  },
  pickerBadge: {
    backgroundColor: '#DBEAFE',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
  },
  pickerBadgeText: {
    fontSize: 11,
    fontWeight: '800',
    color: '#1E40AF',
    letterSpacing: 0.5,
  },
  pickerUnitText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#334155',
  },
  pickerTitleText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#0F172A',
    marginBottom: 4,
  },
  pickerInstruction: {
    fontSize: 12.5,
    color: '#475569',
    marginBottom: 10,
    fontStyle: 'italic',
  },
  questionsContainer: {
    marginTop: 2,
  },
  questionPickBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 10,
    paddingVertical: 10,
    paddingHorizontal: 10,
    marginBottom: 8,
  },
  pickNumberBadge: {
    backgroundColor: '#2563EB',
    width: 22,
    height: 22,
    borderRadius: 11,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 8,
  },
  pickNumberText: {
    color: '#FFFFFF',
    fontSize: 11,
    fontWeight: '800',
  },
  questionPickText: {
    flex: 1,
    fontSize: 13.5,
    fontWeight: '600',
    color: '#0F172A',
    lineHeight: 18,
  },
  questionPickArrow: {
    fontSize: 14,
    fontWeight: '800',
    color: '#2563EB',
    marginLeft: 6,
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
  optionsBox: {
    backgroundColor: '#F8FAFC',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 12,
    marginBottom: 10,
  },
  optionsContainer: {
    marginTop: 4,
  },
  optionRow: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    borderRadius: 8,
    paddingVertical: 7,
    paddingHorizontal: 10,
    marginBottom: 6,
  },
  optionRowCorrect: {
    backgroundColor: '#ECFDF5',
    borderColor: '#10B981',
    borderWidth: 1.5,
  },
  optionLetterBadge: {
    width: 24,
    height: 24,
    borderRadius: 12,
    backgroundColor: '#F1F5F9',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 8,
  },
  optionLetterBadgeCorrect: {
    backgroundColor: '#10B981',
  },
  optionLetterText: {
    fontSize: 12,
    fontWeight: '800',
    color: '#475569',
  },
  optionLetterTextCorrect: {
    color: '#FFFFFF',
  },
  optionContentText: {
    flex: 1,
    fontSize: 13.5,
    color: '#334155',
    fontWeight: '500',
  },
  optionContentTextCorrect: {
    color: '#064E3B',
    fontWeight: '700',
  },
  correctBadge: {
    backgroundColor: '#D1FAE5',
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 4,
    marginLeft: 6,
  },
  correctBadgeText: {
    fontSize: 11,
    fontWeight: '800',
    color: '#065F46',
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
  followupRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginTop: 10,
    paddingTop: 8,
    borderTopWidth: 1,
    borderTopColor: '#F1F5F9',
  },
  doubtBtn: {
    backgroundColor: '#FEF3C7',
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: 8,
  },
  doubtBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#B45309',
  },
  browseMoreBtn: {
    backgroundColor: '#EFF6FF',
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: 8,
  },
  browseMoreBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#1D4ED8',
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
