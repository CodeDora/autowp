import pywhatkit as kit
import datetime as dt
import time 

# Doğum günü kutlayacak kişinin ismi ve doğum tarihi
ad_soyad = "İbrahim" # adı
dogum_tarihi = "09.03.2023" # mesajın gönderileceği tarih

# Şu anki tarih ve saat bilgisini al
bugun = dt.date.today()
su_an = dt.datetime.now().strftime("%H:%M")

# Doğum gününün yıl dönümü bilgisini oluşturma
dogum_gunu = dt.datetime.strptime(dogum_tarihi, "%d.%m.%Y").date()
dogum_yili = dt.date(bugun.year, dogum_gunu.month, dogum_gunu.day)

# Doğum günü mesajı oluşturma mesaj içeriği
mesaj = f"Merhaba ibrahim {ad_soyad},\n\nBugün /{bugun.strftime('%d.%m.%Y')} tarihi ve saat {su_an} Deneme yav Nice mutlu yıllar dilerim! 🎉🎂"

# Doğum günü mesajını WhatsApp üzerinden gönderme
kit.sendwhatmsg_instantly("+90 Gönderilecek kişinin telefon numarası", mesaj, int(su_an[:2]), int(su_an[3:5]) + 1)

time.sleep(60)
