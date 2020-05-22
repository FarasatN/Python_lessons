yaş = input("Yaınız: ")
print("Demek", yaş, "yaşındasın.")
print("Genç mi yoksa yaşlı mı olduğuna karar veremedim:).")

# Kullanıcıdan dairenin çapını girmesini istiyoruz.
diametr = input("Dairenin diametri: ")
# Kullanıcının verdiği çap bilgisini kullanarak
# yarıçapı hesaplayalım. Buradaki int() fonksiyonunu
# ilk kez görüyoruz. Biraz sonra bunu açıklayacağız
radius = int(diametr) / 2
# pi sayımız sabit
pi = 3.14159
# Yukarıdaki bilgileri kullanarak artık
# dairenin alanını hesaplayabiliriz
sahe = pi * (radius ** 2)
# Son olarak, hesapladığımız alanı yazdırıyoruz
print("diametr", diametr, "cm olan dairenin sahesi: ", sahe, "cm2'dir")

sayı = input("Lütfen bir sayı girin: ")
# Girilen sayının karesini bulmak için sayı değişkeninin 2.
# kuvvetini alıyoruz. Aynı şeyi pow() fonksiyonu ile de
# yapabileceğimizi biliyorsunuz. Örn.: pow(sayı, 2)
print("Girdiğiniz sayının karesi: ", int(sayı) ** 2)

sayı1 = input("Toplama işlemi için ilk sayıyı girin: ")
sayı2 = input("Toplama işlemi için ikinci sayıyı girin: ")
print(int(sayı1), "+", int(sayı2), "=", int(sayı1) + int(sayı2))

sayı = 12345678901234
kardiz = str(sayı)
print(len(kardiz))
sayı = 12345678901234
print(len(str(sayı)))
print(len(str(12345678901234)))

# Her bir ayın kaç gün çektiğini tanımlıyoruz
ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
nisan = haziran = eylül = kasım = 30
şubat = 28
# Doğalgazın vergiler dahil metreküp fiyatı
birimFiyat = 0.79
# Kullanıcı ayda ne kadar doğalgaz tüketmiş?
aylıkSarfiyat = input("Aylık doğalgaz sarfiyatınızı metreküp olarak giriniz: ")
# Kullanıcı hangi aya ait faturasını öğrenmek istiyor?
dönem = input("""Hangi aya ait faturayı hesaplamak istersiniz?
(Lütfen ay adını tamamı küçük harf olacak şekilde giriniz)\n""")
# Yukarıdaki input() fonksiyonundan gelen veriyi
# Python'ın anlayabileceği bir biçime dönüştürüyoruz
ay = eval(dönem)
# Kullanıcının günlük doğalgaz sarfiyatı
günlükSarfiyat = int(aylıkSarfiyat) / ay
# Fatura tutarı
fatura = birimFiyat * günlükSarfiyat * ay
print("günlük sarfiyatınız: \t", günlükSarfiyat, " metreküp\n",
      "tahmini fatura tutarı: \t", fatura, " TL", sep="")
print("""
Basit bir hesap makinesi uygulaması.
İşleçler:
+
-
*
/
toplama
çıkarma
çarpma
bölme
Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")
veri = input("İşleminiz: ")
hesap = eval(veri)
print(hesap)

d1 = """
Python'da ekrana çıktı verebilmek için print() adlı bir
fonksiyondan yararlanıyoruz. Bu fonksiyonu şöyle kullanabilirsiniz:
>>> print("Merhaba Dünya")
Şimdi de aynı kodu siz yazın!
>>> """
girdi = input(d1)
exec(girdi)
d2 = """
Gördüğünüz gibi print() fonksiyonu, kendisine
parametre olarak verilen değerleri ekrana basıyor.
Böylece ilk dersimizi tamamlamış olduk. Şimdi bir
sonraki dersimize geçebiliriz."""
print(d2)

#Öncelikle kullanıcıdan bir internet adresi girmesini istiyoruz
url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")
#Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
print("Hata! Google Chrome {} sitesini bulamadı".format(url))
print("Hata! Google Chrome '{}' sitesini bulamadı".format(url))
