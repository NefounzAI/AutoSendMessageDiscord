# Auto Message Discord With Auth

Script Python sederhana untuk mengirim pesan otomatis ke channel Discord menggunakan **Authorization Token** melalui Discord API.

⚠️ **Peringatan:**
Penggunaan token akun (self automation) dapat melanggar Terms of Service Discord. Gunakan hanya untuk tujuan edukasi atau testing.

---

## ✨ Fitur

* Mengirim pesan otomatis ke channel Discord
* Menggunakan **Authorization Token**
* Interval pengiriman pesan yang dapat diatur
* Menampilkan status response dari API
* Pesan notifikasi saat sistem aktif dan berhenti

---

## 📦 Requirements

* Python 3.8+
* Library `requests`
* Library `time`

Install dependency:

```bash
pip install requests
```
```bash
pip install time
```

---

## 📁 Struktur Script

```python
import requests
import time

url = "(https://discord.com/api/v9/channels/CHANNEL_ID/messages)"

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
```

---

## ⚙️ Konfigurasi

Ganti bagian berikut pada script:

### URL Channel

```python
url = "https://discord.com/api/v9/channels/CHANNEL_ID/messages"
```

### Authorization Token

```python
headers = {
    "Authorization": "TokenAuthorizationTokenHere"
}
```

Isi dengan token akun Discord kamu.

---

## ▶️ Cara Menjalankan

1. Clone repository

```bash
git clone https://github.com/username/repository-name.git
```

2. Masuk ke folder project

```bash
cd repository-name
```

3. Jalankan script

```bash
python sendmsg.py
```

---

## ⏱ Mengatur Interval Pesan

Interval pesan diatur di bagian:

```python
time.sleep(14)
```

Contoh:

| Interval | Kode             |
| -------- | ---------------- |
| 10 detik | `time.sleep(10)` |
| 30 detik | `time.sleep(30)` |
| 1 menit  | `time.sleep(60)` |

---

## 🖥 Contoh Output

```
Status: 200 | Pesan: 🟢 Founz System Activated
Status: 200 | Pesan: wb
Status: 200 | Pesan: wb
Status: 200 | Pesan: wb
```

---

## 🛑 Menghentikan Program

Tekan:

```
CTRL + C
```

Program akan mengirim pesan:

```
🔴 Founz System Stopped
```

---

## ⚠️ Disclaimer

Project ini dibuat hanya untuk **pembelajaran mengenai HTTP request dan Discord API**.
Segala bentuk penyalahgunaan adalah tanggung jawab pengguna.

---

## 📄 License

Free to use for educational purposes.
