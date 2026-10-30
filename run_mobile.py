"""Launch the BrightPath Mobile App simulator in your browser."""
import http.server
import os
import socketserver
import webbrowser
from pathlib import Path

PORT = 8080
DIRECTORY = Path(__file__).parent / "mobile_app"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)


def main():
    print(f"\n" + "=" * 56)
    print(f"  BrightPath Mobile App Simulator")
    print(f"  URL: http://localhost:{PORT}/mobile_preview.html")
    print(f"  Model: Qwen 2.5 0.5B (Active in Ollama)")
    print(f"  Press Ctrl+C in this terminal to stop.")
    print("=" * 56 + "\n")
    webbrowser.open(f"http://localhost:{PORT}/mobile_preview.html")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nSimulator stopped.")


if __name__ == "__main__":
    main()

