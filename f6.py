while True:
	ilk_sayı = input("ilk sayı (Programdan çıkmak için q tuşuna basın): ")
	if ilk_sayı == "q":
		break
	ikinci_sayı = input("ikinci sayı: ")
	try:
		sayı1 = int(ilk_sayı)
		sayı2 = int(ikinci_sayı)
		print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
	except (ValueError, ZeroDivisionError):
		print("Bir hata oluştu!")
		print("Lütfen tekrar deneyin!")


ilk_sayı= input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")
try:
	sayı1 = int(ilk_sayı)
	sayı2 = int(ikinci_sayı)
	print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except (ValueError,ZeroDivisionError) as hata:
	print(hata)


try:
	bölünen = int(input("bölünecek sayı: "))
	bölen = int(input("bölen sayı: "))
except ValueError:
	print("Lütfen sadece sayı girin!")
else:
	try:
		print(bölünen/bölen)
	except ZeroDivisionError:
		print("Bir sayıyı 0'a bölemezsiniz!")


bölünen = int(input("bölünecek sayı: "))
if bölünen == 23:
	raise Exception("Bu programda 23 sayısını görmek istemiyorum!")
bölen = int(input("bölen sayı: "))
print(bölünen/bölen)

tr_karakter = "şçğüöıİ"
parola = input("Parolanız: ")
for i in parola:
	if i in tr_karakter:
		raise TypeError("Parolada Türkçe karakter kullanılamaz!")
	else:
		pass
print("Parola kabul edildi!")


import sys
_2x_metni = """
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı."""
_3x_metni = "Programa hoşgeldiniz."
try:
	if sys.version_info.major < 3:
		print(_2x_metni)
	else:
		print(_3x_metni)
except AttributeError:
	print(_2x_metni)