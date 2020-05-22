brothers = ["meqsed", "feraset", "merdan"]
for rank in range(len(brothers)):
	print("{}. {}".format(rank+1, brothers[rank]))

x=[2,3,4,5]
print(x[-2:])

x=['nerimanov']
for i in x:
	print(i[3:]) 


def listl(str, n):
	return(str[n:])
print(listl('narimanov',3))

x=[1,2,3,4,1]
if x[0]==x[-1]:
	print('true')
else:
	print("false") 


def listl(items):
	if items[0]==items[-1]:
		print('true')
	else:
		print('false')
		return items
listl(input())


def sistem_bilgisi_göster():
	import sys
	print("\nSistemde kurulu Python'ın;")
	print("\tana sürüm numarası:", sys.version_info.major)
	print("\talt sürüm numarası:", sys.version_info.minor)
	print("\tminik sürüm numarası:", sys.version_info.micro)
	print("\nKullanılan işletim sisteminin;")
	print("\tadı:", sys.platform)
sistem_bilgisi_göster()


def length(items):
	c = 0
	for s in items:
		c += 1
	print(c)
length(input())

def çarp(*sayılar):
	sonuç = 1
	for i in sayılar:
		sonuç *= i
	print(sonuç)
çarp(1, 2, 3, 4)

def ismin_ne():
	isim = input("ismin ne? ")
	print(isim)
ismin_ne()


def ismin_ne():
	isim = input("ismin ne? ")
	return isim
ismin_ne()

def listl(items):
	if items[0]==items[-1]:
		print('true')
	else:
		print('false')
		return items
listl(input())

x = []
print('x\'in ilk hali:', x)
def değiştir():
	print('x\'i değiştiriyoruz...')
	x.append(1)
	return x
değiştir()
print('x\'in son hali: ', x)

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}
isimler = ["ahmet", "ışık", "ismail", "çiğdem",
"can", "şule", "iskender"]
print(sorted(isimler, key=lambda x: çevrim.get(x[0])))

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}
isimler = ["ahmet", "ışık", "ismail", "çiğdem",
"can", "şule", "iskender"]
def sırala(eleman):
	return çevrim.get(eleman[0])
print(sorted(isimler, key=sırala))


kod_çözücüler = ['UTF-8', 'cp1254', 'latin-1', 'ASCII']
harf = 'İ'
for kç in kod_çözücüler:
	try:
		print("'{}' karakteri {} ile {} olarak "
		"ve {} sayısıyla temsil edilir.".format(harf, kç,
		harf.encode(kç),
		ord(harf)))
	except UnicodeEncodeError:
		print("'{}' karakteri {} ile temsil edilemez!".format(harf, kç))
	for i in range(128):
	    if i % 4 == 0:
	    	print("\n")
	    	print("{:<3}{:>8}\t".format(i, chr(i)), sep="", end="")
		
					

		
import multiprocessing
print(multiprocessing.cpu_count())
