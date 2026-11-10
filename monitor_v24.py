import subprocess
import time
import os
import sys

TAG = "v2.4"
URL = f"https://github.com/Srijaisuryaa007/SLM/releases/download/{TAG}/BrightPath-Qwen-Offline.apk"
APK_OUT = "BrightPath-v2.4.apk"

def check_url_ready():
    res = subprocess.run(["curl.exe", "-sI", f"https://github.com/Srijaisuryaa007/SLM/releases/tag/{TAG}"], capture_output=True, text=True)
    return "HTTP/1.1 200" in res.stdout or "HTTP/2 200" in res.stdout

def download_and_install():
    start = time.time()
    print("=" * 60)
    print("🚀 Monitoring GitHub Actions CI Build for v2.4 (All Book-Back & End-of-Lesson Exercises)...")
    print("=" * 60)
    while True:
        if check_url_ready():
            print(f"\n🎉 GitHub Release {TAG} is published! Downloading APK...")
            dl_res = subprocess.run(["curl.exe", "-L", "-o", APK_OUT, URL])
            if dl_res.returncode == 0 and os.path.exists(APK_OUT) and os.path.getsize(APK_OUT) > 500 * 1024 * 1024:
                file_mb = os.path.getsize(APK_OUT) / (1024 * 1024)
                print(f"\n✅ Downloaded {APK_OUT} ({file_mb:.1f} MB) successfully!")
                print("\n📱 Installing on connected OnePlus phone via USB ADB...")
                subprocess.run(["adb", "shell", "settings", "put", "global", "verifier_verify_adb_installs", "0"])
                subprocess.run(["adb", "shell", "settings", "put", "global", "package_verifier_enable", "0"])
                inst_res = subprocess.run(["adb", "install", "-r", "-d", "-g", APK_OUT], capture_output=True, text=True)
                print(inst_res.stdout)
                if inst_res.stderr:
                    print(inst_res.stderr)
                if "Success" in inst_res.stdout:
                    print("🎯 v2.4 APK installed successfully on device!")
                    print("🚀 Launching English Class 9 AI Assistant...")
                    subprocess.run(["adb", "shell", "am", "force-stop", "com.brightpathapp"])
                    subprocess.run(["adb", "shell", "am", "start", "-n", "com.brightpathapp/.MainActivity"])
                    return True
                else:
                    print("Install output did not indicate success. Please check device.")
                    return False
            else:
                print("Download incomplete, retrying...")
        elapsed = int(time.time() - start)
        print(f"[{elapsed}s] Waiting for {TAG} build and release on GitHub...", end="\r")
        sys.stdout.flush()
        time.sleep(25)

if __name__ == "__main__":
    download_and_install()
