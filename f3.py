izinli_karakterler = "0123456789+-/*=%// "
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
while True:
    veri = input("İşleminiz: ")
    if veri == "q":
        print("çıkılıyor...")
        break
    for s in veri:
        if s not in izinli_karakterler:
            print("Neyin peşindesin?!")
            quit()
    hesap = eval(veri)
    print(hesap)


for i in range(3):
    parola = input("parola belirleyin: ")
    if i == 2:
        print("parolayı 3 kez yanlış girdiniz.",
        "Lütfen 30 dakika sonra tekrar deneyin!")
    elif not parola:
        pass
    elif len(parola) in range(3, 8):
        print("Yeni parolanız", parola)
        break
    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")



for i in range(3):
    print(i)
    parola = input("parola belirleyin: ")
    if i == 2:
        print("parolayı 3 kez yanlış girdiniz.",
        "Lütfen 30 dakika sonra tekrar deneyin!")
    elif not parola:
        pass
    elif len(parola) in range(3, 8):
        print("Yeni parolanız", parola)
        break
    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")