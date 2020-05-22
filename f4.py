while True:
    sayı = int(input("Bir sayı girin: "))
    if sayı == 0:
        break
    elif sayı < 0:
        pass
    else:
        print(sayı)


while True:
    s = input("Bir sayı girin: ")
    if s == "iptal":
        break																									
    if len(s) <= 3:
        continue
    print("En fazla üç haneli bir sayı girebilirsiniz.")



d1 = open("isimler1.txt",encoding="utf-8") # dosyayı açıyoruz
d1_satırlar = d1.readlines() # satırları okuyoruz
d2 = open("isimler2.txt",encoding="utf-8")
d2_satırlar = d2.readlines()
for i in d2_satırlar:
    if not i in d1_satırlar:
        print(i)
d1.close()
d2.close()