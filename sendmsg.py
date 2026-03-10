import requests
import time

url = "UrlMessageHere/tokenid"

headers = {
    "Authorization": "TokenAuthorizationTokenHere"
}

def send(msg):
    payload = {"content": msg}
    r = requests.post(url, json=payload, headers=headers)
    print("Status:", r.status_code, "| Pesan:", msg)

try:
    send("🟢 Founz System Activated")

    while True:
        send("wb")
        time.sleep(14)

except KeyboardInterrupt:
    send("🔴 Founz System Stopped")
    print("Program dihentikan.")