import threading
import urllib.request
import time

def keep_alive():
    url = "https://www.pendoessence.co.tz/"
    while True:
        try:
            urllib.request.urlopen(url, timeout=10)
            print("✅ Keep-alive ping sent")
        except Exception as e:
            print(f"⚠️ Ping failed: {e}")
        time.sleep(300)  # kila dakika 5

def start():
    t = threading.Thread(target=keep_alive, daemon=True)
    t.start()