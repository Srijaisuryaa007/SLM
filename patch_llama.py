import os
import sys

def patch_llama():
    candidates = [
        "BrightPathApp/node_modules/llama.rn/android/src/main/java/com/rnllama/LlamaContext.java",
        "mobile_app/node_modules/llama.rn/android/src/main/java/com/rnllama/LlamaContext.java",
    ]
    
    target_path = None
    for c in candidates:
        if os.path.exists(c):
            target_path = c
            break

    if not target_path:
        print("Notice: LlamaContext.java not found in known paths, skipping patch.")
        return

    print(f"Patching {target_path}...")
    with open(target_path, "r", encoding="utf-8") as f:
        code = f.read()

    if "Auto-extracting model asset" in code:
        print("LlamaContext.java is already patched.")
        return

    target = '    this.id = id;\n    this.context = initContext(\n      // String model,\n      params.getString("model"),'
    
    replacement = '''    this.id = id;
    String modelPath = params.getString("model");
    try {
      File checkF = new File(modelPath);
      if (!checkF.isAbsolute() || !checkF.exists()) {
        String assetName = checkF.getName();
        File destF = new File(reactContext.getFilesDir(), assetName);
        if (!destF.exists() || destF.length() < 100000000L) {
          Log.i("RNLlama", "Auto-extracting model asset: " + assetName);
          java.io.InputStream in = reactContext.getAssets().open(assetName);
          java.io.OutputStream out = new java.io.FileOutputStream(destF);
          byte[] b = new byte[2 * 1024 * 1024];
          int r;
          while ((r = in.read(b)) != -1) {
            out.write(b, 0, r);
          }
          out.flush();
          out.close();
          in.close();
          Log.i("RNLlama", "Extracted model successfully: " + destF.getAbsolutePath());
        }
        modelPath = destF.getAbsolutePath();
      }
    } catch (Exception e) {
      Log.w("RNLlama", "Asset resolution warning: " + e.getMessage());
    }
    this.context = initContext(
      // String model,
      modelPath,'''

    if target in code:
        code = code.replace(target, replacement)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(code)
        print("Successfully patched LlamaContext.java for Android asset loading!")
    else:
        print("Warning: target signature not matched in LlamaContext.java.")

if __name__ == "__main__":
    patch_llama()
