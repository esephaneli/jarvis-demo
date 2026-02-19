# ============================================
#  J.A.R.V.I.S - Samsung J5 AI Asistan
#  Mimari Özet (LinkedIn için)
#  Tam kod: ~500 satır Python
# ============================================
#
#  Gereksinimler:
#  - Root'lu Android telefon
#  - Termux (apt-android-5)
#  - Python 3 + requests kütüphanesi
#  - Gemini API key (ücretsiz)
#
#  Kurulum:
#  pkg install python espeak -y
#  pip install requests
# ============================================

import subprocess, requests, os
from datetime import datetime

# ============ AYARLAR ============
GEMINI_API_KEY = "API_KEY_BURAYA"
JARVIS_ADI = "Jarvis"
SAHIP_ADI = "Efendim"

# ============ SES SİSTEMİ ============
def konus(metin):
    """eSpeak TTS ile sesli çıktı (Android 6'da sınırlı)"""
    print(f"[{JARVIS_ADI}]: {metin}")
    os.system(f'espeak -v tr "{metin}" 2>/dev/null')

def dinle():
    """Kullanıcıdan girdi al (klavye + mikrofon)"""
    return input("Sen > ").strip().lower()

# ============ ROOT KONTROL ============
def root_komut(komut):
    """Root yetkisiyle sistem komutu çalıştır"""
    sonuc = subprocess.run(
        ["su", "-c", komut],
        capture_output=True, text=True
    )
    return sonuc.stdout.strip()

# Örnekler:
def fener_ac():
    root_komut("echo 1 > /sys/class/leds/flashlight/brightness")

def pil_durumu():
    seviye = root_komut("cat /sys/class/power_supply/battery/capacity")
    return f"Pil seviyesi: %{seviye}"

def arama_yap(numara):
    root_komut(f"am start -a android.intent.action.CALL -d tel:{numara}")

def uygulama_ac(paket):
    root_komut(f"monkey -p {paket} 1")

# ============ GEMİNİ AI ============
def gemini_sor(soru):
    """Gemini 2.5 Flash API ile akıllı yanıt"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{
            "parts": [{"text": f"Sen JARVIS adında bir AI asistansın. Kısa ve öz cevap ver: {soru}"}]
        }]
    }
    r = requests.post(url, json=payload, timeout=15)
    return r.json()["candidates"][0]["content"]["parts"][0]["text"]

# ============ KOMUT İŞLEME ============
def komut_isle(komut):
    """Ana komut yönlendirici - regex + keyword matching"""

    if "merhaba" in komut:
        konus("Merhaba! Size nasıl yardımcı olabilirim?")

    elif "saat" in komut:
        konus(datetime.now().strftime("Saat %H:%M"))

    elif "fener ac" in komut:
        fener_ac()
        konus("Fener açıldı.")

    elif "pil" in komut:
        konus(pil_durumu())

    elif "ara " in komut:
        numara = komut.replace("ara ", "")
        arama_yap(numara)

    elif "hava durumu" in komut:
        # wttr.in API - ücretsiz, key gerektirmez
        r = requests.get("http://wttr.in/Istanbul?format=%t+%C&lang=tr")
        konus(f"Hava durumu: {r.text.strip()}")

    else:
        # Tanınmayan her şey → Gemini AI
        yanit = gemini_sor(komut)
        konus(yanit)

# ============ ANA DÖNGÜ ============
def main():
    konus("JARVIS aktif. Emrinize amadeyim!")
    while True:
        komut = dinle()
        if komut in ["kapat", "çıkış"]:
            konus("Görüşmek üzere!")
            break
        komut_isle(komut)

if __name__ == "__main__":
    main()

# ============================================
#  MİMARİ ÖZET:
#
#  Kullanıcı (ses/klavye)
#       │
#       ▼
#  Komut İşleme (keyword matching)
#       │
#       ├── Telefon Kontrolü (root komutları)
#       │   ├── Fener (sysfs)
#       │   ├── Arama/SMS (am start)
#       │   ├── Uygulama (monkey)
#       │   ├── Parlaklık/Ses (settings)
#       │   └── Pil/WiFi (cat/dumpsys)
#       │
#       ├── Yerel Komutlar
#       │   ├── Saat/Tarih (datetime)
#       │   ├── Hava Durumu (wttr.in)
#       │   └── Not Al/Oku (dosya)
#       │
#       └── Gemini AI (tanınmayan her şey)
#           └── gemini-2.5-flash API
#
#       │
#       ▼
#  Sesli/Yazılı Yanıt (eSpeak TTS)
# ============================================
