# BrightPath Mobile: On-Device SLM App (< 1 GB)

An offline, on-device mobile AI assistant for students powered by **Qwen 2.5 0.5B Instruct** and local keyword RAG.

---

## 📱 App Size Breakdown

| Component | Size |
|---|---|
| Native App (React Native runtime + UI) | ~35 MB |
| Local Facts Knowledge Base (`facts.json`) | < 1 KB |
| **Qwen 2.5 0.5B Instruct (Q4_K_M GGUF)** | **~390 MB** |
| **Total Distributed App Size** | **~425 MB** *(Well under the 1 GB target)* |

---

## ⚡ How It Works On-Device (Zero Server Cost, 100% Offline)

1. **FIND**: When a student asks a question on their phone, `src/rag/finder.js` performs an instant keyword & entity match on `assets/facts.json`.
2. **BUILD**: Constructs the Qwen ChatML prompt with system instructions and verified course facts (`src/prompt/prompt.js`).
3. **ASK**: `llama.rn` executes the ~390 MB `.gguf` directly on the phone's CPU/GPU with real-time token streaming.

---

## 🚀 Quick Testing (Desktop / Browser)

You can preview and test the mobile application right now:

1. **Interactive Mobile Handset Preview**:
   Double click [`mobile_preview.html`](file:///c:/ds/mini_brightpath/mobile_app/mobile_preview.html) to open the iPhone mockup in your browser. It connects directly to your local Ollama instance running `qwen2.5:0.5b`!

2. **Command Line Test**:
   ```bash
   python ask.py --model qwen2.5:0.5b -q "What is the fee for Class 9 science?"
   ```

---

## 🛠️ Building for Native Android / iOS

### Prerequisites
* Node.js v18+ (You have v24 installed)
* Android Studio (for Android APK) or Xcode (for iOS)

### Step 1: Install Dependencies
```bash
cd mobile_app
npm install
```

### Step 2: Add the Model to App Assets
Place your fine-tuned GGUF file exported from Google Colab into:
```
mobile_app/assets/brightpath-qwen-0.5b.Q4_K_M.gguf
```

### Step 3: Run on Android Emulator or Connected Phone
```bash
npm run android
```
Or for iOS:
```bash
npm run ios
```

