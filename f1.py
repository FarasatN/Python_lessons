kullanıcı_adı = input("Kullanıcı adınız: ")
parola = input("Parolanız: ")
if kullanıcı_adı == "aliveli":
    if parola == "12345678":
        print("Programa hoşgeldiniz")
    else:
        print("Yanlış kullanıcı adı veya parola!")
else:
    print("Yanlış kullanıcı adı veya parola!")

    
kullanıcı_adı = input("Kullanıcı adınız: ")
parola = input("Parolanız: ")
if kullanıcı_adı == "aliveli" and parola == "12345678":
    print("Programa hoşgeldiniz")
else:
    print("Yanlış kullanıcı adı veya parola!")


x = int(input("Notunuz: "))
if x > 100 or x < 0:
    print("Böyle bir not yok")
elif x >= 90 and x <= 100:
    print("A aldınız.")
elif x >= 80 and x <= 89:
    print("B aldınız.")
elif x >= 70 and x <= 79:
    print("C aldınız.")
elif x >= 60 and x <= 69:
    print("D aldınız.")
elif x >= 0 and x <= 59:
    print("F aldınız.")

    x = int(input("Notunuz: "))
if x > 100 or x < 0:
    print("Böyle bir not yok")
elif x >= 90 <= 100:
    print("A aldınız.")
elif x >= 80 <= 89:
    print("B aldınız.")
elif x >= 70 <= 79:
    print("C aldınız.")
elif x >= 60 <= 69:
    print("D aldınız.")
elif x >= 0 <= 59:
    print("F aldınız.")

x = int(input("Notunuz: "))
if x > 100 or x < 0:
    print("Böyle bir not yok")
#90 sayısı x'ten küçük veya x'e eşit,
#x sayısı 100'den küçük veya 100'e eşit ise,
#Yani x, 90 ile 100 arasında bir sayı ise
elif 90 <= x <= 100:
    print("A aldınız.")
#80 sayısı x'ten küçük veya x'e eşit,
#x sayısı 89'dan küçük veya 89'a eşit ise,
#Yani x, 80 ile 89 arasında bir sayı ise
elif 80 <= x <= 89:
    print("B aldınız.")
elif 70 <= x <= 79:
    print("C aldınız.")
elif 60 <= x <= 69:
    print("D aldınız.")
elif 0 <= x <= 59:
    print("F aldınız.")




    giriş = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) karesini hesapla
(6) kare kök hesapla
"""
print(giriş)

while True:
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if soru == "q":
        print("çıkılıyor...")
        break

    elif soru == "1":
        sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
        sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)
    elif soru == "2":
        sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
        sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)
    elif soru == "3":
        sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
        sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
        print(sayı5, "x", sayı6, "=", sayı5 * sayı6)
    elif soru == "4":
        sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
        sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
        print(sayı7, "/", sayı8, "=", sayı7 / sayı8)
    elif soru == "5":
        sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
        print(sayı9, "sayısının karesi =", sayı9 ** 2)
    elif soru == "6":
        sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
        print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)
    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)



tekrar = 1
while tekrar <= 3:
    tekrar += 1
    input("Nasılsınız, iyi misiniz?")

import sys
_2x_metni = """
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı."""
_3x_metni = "Programa hoşgeldiniz."
if sys.version_info.major < 3:
    print(_2x_metni)
else:
    print(_3x_metni)
    
