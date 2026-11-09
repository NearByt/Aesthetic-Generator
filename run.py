import os
import sys
import webbrowser
import threading
import time
import uvicorn
from pathlib import Path

# Ensure package root is in sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Ensure ffmpeg binary exists
from backend.video_engine import setup_ffmpeg

def open_browser(port):
    time.sleep(1.2)
    url = f"http://127.0.0.1:{port}"
    print(f"\n=======================================================")
    print(f"  ✨ Liquid Clip Studio is Live!")
    print(f"  🌐 URL: {url}")
    print(f"  ⚡ Press Ctrl+C in terminal to stop server")
    print(f"=======================================================\n")
    try:
        webbrowser.open(url)
    except Exception:
        pass

if __name__ == "__main__":
    setup_ffmpeg()
    port = 8000
    
    # Check port availability or use fallback
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
        s.close()
    except OSError:
        port = 8080

    threading.Thread(target=open_browser, args=(port,), daemon=True).start()
    
    # Run server
    uvicorn.run("backend.main:app", host="127.0.0.1", port=port, log_level="info")
