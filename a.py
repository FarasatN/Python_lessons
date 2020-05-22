yaş = 15
print("""Programa hoşgeldiniz!
Programımızı kullanabilmek için en az
13 yaşında olmalısınız.""")
print("Yaşınız: ", yaş)

print("""Programa hoşgeldiniz!
Programımızı kullanabilmek için en az
13 yaşında olmalısınız.""")
print("Lütfen yaşınızı girin. \n")
yaş = input("Yaşınız: \t")
print("Yaşınız: ", yaş)


sayı = int(input("Bir sayı giriniz: "))
if sayı > 10:
    print("Girdiğiniz sayı 10'dan büyüktür!")
if sayı < 10:
    print("Girdiğiniz sayı 10'dan küçüktür!")
if sayı == 10:
    print("Girdiğiniz sayı 10'dur!")
    
print("""
Dünyanın en gelişmiş e.posta hizmetine
hoşgeldiniz. Yalnız hizmetimizden
yararlanmak için önce sisteme giriş
yapmalısınız.
""")
parola = input("Parola: ")
if parola == "12345678":
    print("Sisteme Hoşgeldiniz!")
if parola != "12345678":
    print("Ne yazık ki yanlış parola girdiniz!")


yaş = int(input("Yaşınız: "))
if yaş == 18:
    print("18 iyidir!")
if yaş < 0:
    print("Yok canım, daha neler!...")
if yaş < 18:
    print("Genç bir kardeşimizsin!")
if yaş > 18:
    print("Eh, artık yaş yavaş yavaş kemale eriyor!")

yaş = int(input("Yaşınız: "))
if yaş == 18:
    print("18 iyidir!")
elif yaş < 0:
    print("Yok canım, daha neler!...")
elif yaş < 18:
    print("Genç bir kardeşimizsin!")
elif yaş > 18:
    print("Eh, artık yaş yavaş yavaş kemale eriyor!")

a = int(input("Bir sayı giriniz: "))
if a < 50:
    print("verdiğiniz sayı 100'den küçüktür.")
elif a < 100:
    print("verdiğiniz sayı 50'den küçüktür.")
elif a == 100:
    print("verdiğiniz sayı 100'dür.")
elif a > 150:
    print("verdiğiniz sayı 150'den büyüktür.")
elif a > 100:
    print("verdiğiniz sayı 100'den büyüktür.")
    
soru = input("Bir meyve adı söyleyin bana:")
if soru == "elma":
    print("evet, elma bir meyvedir...")
elif soru == "karpuz":
    print("evet, karpuz bir meyvedir...")
elif soru == "armut":
    print("evet, armut bir meyvedir...")
else:
    print(soru, "gerçekten bir meyve midir?")

boy = int(input("boyunuz kaç cm?"))
if boy < 170:
    print("boyunuz kısa")
elif boy < 180:
    print("boyunuz normal")
else:
    print("boyunuz uzun")


kullanıcı_adı = input("Kullanıcı adınız: ")
parola= input("Parolanız: ")
toplam_uzunluk = len(kullanıcı_adı) + len(parola)
mesaj = "Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor!"
print(mesaj.format(toplam_uzunluk))
if toplam_uzunluk > 40:
    print("Kullanıcı adınız ile parolanızın ",
"toplam uzunluğu 40 karakteri geçmemeli!")
else:
    print("Sisteme hoşgeldiniz!")


sayı = int(input("Bir sayı girin: "))
if sayı % 2 == 0:
    print("Girdiğiniz sayı bir çift sayıdır.")
else:
    print("Girdiğiniz sayı bir tek sayıdır.")

parola = "xyz05"
soru = input("parolanız: ")
if soru == parola:
    print("doğru parola!")
elif soru != parola:
    print("yanlış parola!")


    isim = input("İsminiz: ")
print(isim == "Ferhat")


kullanıcı = input("Kullanıcı adınız: ")
if bool(kullanıcı) == True:
    print("Teşekkürler!")
else:
    print("Kullanıcı adı alanı boş bırakılamaz!")

    kullanıcı = input("Kullanıcı adınız: ")
if kullanıcı:
    print("Teşekkürler!")


