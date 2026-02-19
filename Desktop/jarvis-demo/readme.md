'''
🤖 J.A.R.V.I.S — DEMO


Çekmecede unutulmuş 2015 model bir telefonu kişisel yapay zeka asistanına dönüştüren proje.


🎯 Nedir?
JARVIS, eski bir Samsung Galaxy J5 (SM-J500F) üzerinde çalışan, sesli komut alabilen ve Gemini AI destekli kişisel asistan. Root erişimi + Termux + Python ile tamamen ücretsiz olarak çalışır.

📱 Donanım
TelefonSamsung Galaxy J5 (2015) SM-J500FİşlemciSnapdragon 410 Quad-core 1.2 GHzRAM1.5 GBAndroid6.0.1 MarshmallowRootEvet (gerekli)

⚡ Özellikler
📞 Telefon Kontrolü (Root)

Fener aç/kapat
Telefon araması yapma
SMS gönderme
Uygulama açma (Chrome, YouTube, WhatsApp, Kamera vb.)
Ekran parlaklığı ve ses ayarı
Pil durumu sorgulama
WiFi / IP bilgisi
Ekran görüntüsü alma

🧠 Yapay Zeka (Gemini 2.5 Flash)

Her türlü soruya akıllı yanıt
Türkçe doğal dil desteği
Tanınmayan komutlar otomatik olarak AI'a yönlenir

🌤️ Günlük Araçlar

Saat ve tarih
Hava durumu (wttr.in API)
Not alma ve okuma

🎤 Giriş/Çıkış

Sesli komut: Android klavye mikrofonu ile
Yazılı komut: Termux terminal
Sesli yanıt: eSpeak TTS (Android 6'da sınırlı destek)


Kullanici (ses/klavye)
       |
Komut Isleme (keyword matching)
       |
       |-- Telefon Kontrolu (root)
       |     |-- Fener: /sys/class/leds/
       |     |-- Arama/SMS: am start intent
       |     |-- Uygulama: monkey -p paket
       |     |-- Parlaklik/Ses: settings put
       |     |-- Pil/WiFi: cat / dumpsys
       |
       |-- Yerel Komutlar
       |     |-- Saat/Tarih: datetime
       |     |-- Hava Durumu: wttr.in API
       |     |-- Not Al/Oku: dosya sistemi
       |
       |-- Gemini AI (fallback)
             |-- gemini-2.5-flash API
       |
Sesli/Yazili Yanit (eSpeak TTS + terminal)


🛠️ Kurulum
1. Termux Kur
Android 5-6 için özel sürüm gerekli:
termux-app_v0.119.0-beta.3+apt-android-5-github-debug_universal.apk
→ github.com/termux/termux-app/releases
2. Paketleri Yükle
bashpkg update && pkg upgrade -y
pkg install python espeak -y
pip install requests
3. Depolama İzni
bashtermux-setup-storage
4. Gemini API Key Al
https://aistudio.google.com/app/apikey
Ücretsiz. Kodu aç, GEMINI_API_KEY satırına yapıştır.
5. Çalıştır
bash python jarvis.py

🔧 Teknik Detaylar

Dil: Python 3
AI: Google Gemini 2.5 Flash (ücretsiz API)
TTS: eSpeak (Türkçe)
Hava Durumu: wttr.in (ücretsiz, key gerektirmez)
Telefon Kontrolü: Android root su -c komutları
Terminal: Termux (apt-android-5 sürümü)
Toplam Maliyet: 0 TL


⚠️ Bilinen Sınırlamalar

TTS ses çıkışı: Termux + Android 6 kombinasyonunda eSpeak ses çıkışı çalışmıyor.
Termux:API: Android 6'da parsing hatası veriyor, bu yüzden mikrofon ve TTS için alternatif yollar kullanılıyor.
Gemini API: İnternet bağlantısı gerektirir. Çevrimdışıyken sadece kural tabanlı komutlar çalışır.



📄 Lisans
Bu proje açık kaynaklıdır. Dilediğiniz gibi kullanabilir ve geliştirebilirsiniz.
'''
