metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
edilmesi neredeyse bir gelenek halini almıştır."""
harf = input("Sorgulamak istediğiniz harf: ")
sayı = 0
for s in metin:
    if harf == s:
        sayı += 1
print(sayı)

metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
edilmesi neredeyse bir gelenek halini almıştır."""
harf = input("Sorgulamak istediğiniz harf: ")
sayı = ''
for s in metin:# metin içinde 's' adını verdiğimiz herbir öğe için
# eğer kullanıcıdan gelen harf 's' ile aynıysa
# kullanıcıdan gelen bu harfi sayı değişkenine yolla
    if harf == s:
        sayı += harf
print(len(sayı))


x = open("isimler1.txt", encoding="utf-8")
harf = input("Sorgulamak istediğiniz harf: ")
sayı = 0
for s in x:
	print(s)
	for a in s:
		print(repr(a))
        if harf == a:
            sayı += 1
print(sayı)
x.close()
    