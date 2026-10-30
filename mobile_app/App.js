import React, { Component } from 'react';
import { StatusBar, View, Text, StyleSheet, ScrollView } from 'react-native';
import ChatScreen from './src/components/ChatScreen';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.warn("ErrorBoundary caught error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <View style={styles.errorContainer}>
          <Text style={styles.errorTitle}>BrightPath Notice</Text>
          <ScrollView>
            <Text style={styles.errorText}>
              {this.state.error ? this.state.error.toString() : 'An error occurred while launching.'}
            </Text>
          </ScrollView>
        </View>
      );
    }
    return this.props.children;
  }
}

export default function App() {
  return (
    <ErrorBoundary>
      <StatusBar barStyle="dark-content" />
      <ChatScreen />
    </ErrorBoundary>
  );
}

const styles = StyleSheet.create({
  errorContainer: {
    flex: 1,
    padding: 24,
    justifyContent: 'center',
    backgroundColor: '#FFFFFF',
  },
  errorTitle: {
    fontSize: 20,
    fontWeight: '700',
    color: '#E11D48',
    marginBottom: 12,
  },
  errorText: {
    fontSize: 14,
    color: '#334155',
    lineHeight: 20,
  },
});
