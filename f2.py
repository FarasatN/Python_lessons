anahtar = 1
while anahtar == 1:
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if soru == "q":
        print("çıkılıyor... ")
        anahtar = 0

while True:
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
    if soru == "q":
        print("çıkılıyor...")
        break

a = 0
while a < 100:
    a += 1
    if a % 2 == 0:
        print(a)

tr_harfler = "şçöğüİı"
for harf in tr_harfler:
    print(harf)


sayılar = "123456789"
for i in sayılar:
    if int(i) > 3:
        print(i)

a = "şçöğüİı"
b = input("Parolanız: ")
for x in b:
    if x in a:
        print("parolada Türkçe karakter kullanılamaz")



while True:
    parola = input("Bir parola belirleyin: ")
    if not parola:
        print("parola bölümü boş geçilemez!")
    elif len(parola) > 8 or len(parola) < 3:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")
    else:
        print("Yeni parolanız", parola)
        break

