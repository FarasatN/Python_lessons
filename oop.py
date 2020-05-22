'''class Calisan():
	kabil=[]

	def __init__(self):
		self.kabil=[]
		
print(Calisan.kabil)

farasat=Calisan()
print(farasat.kabil)'''
"""
min_val = 0 # def min value 
ints = [1, 2, 3, 4, 5, 6] # the list of inputs
 
# loop through each item in ints list
for item in ints:
	# if the current item is less than the item before it and it is less than our current min_val then we assign min_val to that item
	if item < ints[ints.index(item)-1] and item < min_val:
		min_val = item
# print the min_val
print(min_val)


def minimum(list):
  current_min = list[0]  # Start by assuming the first number is smallest
  for num in list:       # Loop through each number in the list
    if num < current_min:
      current_min = num  # Update current_min if current number is less
  return current_min

print minimum([1,2,3,-1])  



def minmax1 (x):
    # this function fails if the list length is 0 
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum: maximum = i
    return (minimum,maximum)

print(minmax1([9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19]))
print(minmax1([1]))
print(minmax1([2, 0, 2, 7, 5, -1, -2]))



x=[12,1,3]
ma=x[0]
mi=x[0]
a=0
for i in len(range(x)):
	a+=1
	if x[a]>ma:
		ma=x[a]
	if x[a]<mi:
		mi=x[a]
	print(ma)
	print(mi)
"""



class Çalışan():
	kabiliyetleri = ['sınıf niteliği']
	def __init__(self):
		self.kabiliyetleri = ['örnek niteliği']

print(Çalışan.kabiliyetleri)
ahmet = Çalışan()
print(ahmet.kabiliyetleri)


class Çalışan():
	personel = []
	def __init__(self, isim):
		self.isim = isim
		self.kabiliyetleri = []
		self.personele_ekle()
	def personele_ekle(self):
		self.personel.append(self.isim)
		print('{} adlı kişi personele eklendi'.format(self.isim))
	def personeli_görüntüle(self):
		print('Personel listesi:')
		for kişi in self.personel:
			print(kişi)
	def kabiliyet_ekle(self, kabiliyet):
		self.kabiliyetleri.append(kabiliyet)
	def kabiliyetleri_görüntüle(self):
		print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
		for kabiliyet in self.kabiliyetleri:
			print(kabiliyet)


class HarfSayacı:
	def __init__(self):
		self.sesli_harfler = 'aeıioöuü'
		self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
		self.sayaç_sesli = 0
		self.sayaç_sessiz = 0
	def kelime_sor(self):
		return input('Bir kelime girin: ')
	def seslidir(self, harf):
		return harf in self.sesli_harfler
	def sessizdir(self, harf):
		return harf in self.sessiz_harfler
	def artır(self):
		for harf in self.kelime:
			if self.seslidir(harf):
				self.sayaç_sesli += 1
			if self.sessizdir(harf):
				self.sayaç_sessiz += 1
			return (self.sayaç_sesli, self.sayaç_sessiz)
		def ekrana_bas(self):
			sesli, sessiz = self.artır()
			mesaj = "{} kelimesinde {} sesli {} sessiz harf var."
			print(mesaj.format(self.kelime, sesli, sessiz))
		def çalıştır(self):
			self.kelime = self.kelime_sor()
			self.ekrana_bas()
if __name__ == '__main__':
	sayaç = HarfSayacı()
	sayaç.çalıştır()