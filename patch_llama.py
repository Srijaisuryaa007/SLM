import os
import sys
import re

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

    print(f"Reading {target_path}...")
    with open(target_path, "r", encoding="utf-8") as f:
        code = f.read()

    if "Auto-extracting model asset" in code:
        print("LlamaContext.java is already patched.")
        return

    # Normalize line endings
    code_normalized = code.replace("\r\n", "\n")

    # Match: this.id = id; ... this.context = initContext( ... params.getString("model"),
    pattern = r'(this\.id\s*=\s*id;\s*)(this\.context\s*=\s*initContext\(\s*(?://[^\n]*\n\s*)?params\.getString\("model"\),)'

    replacement = r'''\1String modelPath = params.getString("model");
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

    new_code, count = re.subn(pattern, replacement, code_normalized)
    if count == 0:
        print("ERROR: Regex pattern failed to match in LlamaContext.java!")
        print("Here are lines 60-75 of the file:")
        lines = code_normalized.split("\n")[55:80]
        for i, l in enumerate(lines, 56):
            print(f"{i}: {l}")
        sys.exit(1)

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(new_code)
    print(f"Successfully applied regex patch to {target_path} (matches: {count})!")

if __name__ == "__main__":
    patch_llama()
