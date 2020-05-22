# l=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
# print(l)
# l2=[(x,y,z) for x in [1,2,3] for y,z in [(1,2),(2,3),(3,4)] if x!=y]
# print(l2)
# k=[[[1,2,3],[2,3,4]],[[1,2,3],[1,1,1]],[[2,2]]]
# print(k)
# print(len(k))
# print(len(k[1]))
# m=[[1,3,5,],[3,4,5],[1,2,3]]
# mt=[[row[i] for row in m] for i in range(3)]
# print(mt)
# del(k[1])
# print(k)
# t=(1,2,3)
# x,y,z=t
# print(x)
# print(z)
# z=10
# print(t)
# t=(x,y,z)
# print(t)
# v=([1,2,3],[3,2,1])
# print(v)
# v[0][1]=100
# print(v)
# s={1,2,3}
# k4=set('farasat')
# k5=set('novruzov')
# print(k4)
# print(k5)
# print(k4-k5)
# print(k4^k5)


# import random
# class Dusman():
# 	def __init__(self, isim="Dusman",kalancan=1000,saldirigucu=40,mermisayisi=45):
# 		self.isim=isim
# 		self.kalancan=kalancan
# 		self.saldirigucu=saldirigucu
# 		self.mermisayisi=mermisayisi

# 	def print(self):
# 		print("Basiliyor...")
# 		print("Isim:",self.isim,"Kalancan:",self.kalancan,"Saldirigucu:",self.saldirigucu,"Mermisayisi:",self.mermisayisi)

# 	def saldir(self):
# 		print(self.isim+"Saldiriyor.")
# 		harcananmermi=random.randrange(0,10)
# 		print(str(harcananmermi)+" kadar harcandi")
# 		self.mermisayisi-=harcananmermi
# 		return (harcananmermi,self.saldirigucu)

# 	def saldiriyaugra(self,harcananmermi,saldirigucu):
# 		print("Vurulduumm")
# 		self.kalancan-=(harcananmermi*saldirigucu)

# 	def mermibitti(self):
# 		if (self.mermisayisi<=0):
# 			print(self.isim+"Konusuyor: mermim bitti cikiyorum")
# 			return True
# 		return False
# 	def hayattami(self):
# 		if (self.kalancan<=0):
# 			print("hayiir..oluyoruummm")

# dusmanlar=[]
# i=0
# while (i<10):
# 	rastgelecan=random.randrange(100,200)
# 	rastgelesaldirigucu=random.randrange(10,20)
# 	rastgelemermi=random.randrange(20,30)
# 	yenidusman=Dusman("Dusman"+str(i+1),rastgelecan,rastgelesaldirigucu,rastgelemermi)
# 	dusmanlar.append(yenidusman)
# 	i+=1
# for dusman in dusmanlar:
# 	dusman.print()
# i=0
# while (i<3):
# 	randomdusman1=random.randrange(0,10)
# 	randomdusman2=random.randrange(0,10)
# 	donendeger=dusmanlar[randomdusman1].saldir()
# 	dusmanlar[randomdusman2].saldiriyaugra(donendeger[0],donendeger[1])
# 	print("Round bitti...")
# 	i+=1
# dusman1=Dusman("Ali",2000,30,50)
# print("\n\n\n\aDusman1___________________________________")
# dusman1.print()

# dusman3=Dusman()
# print("Dusman3___________________________________")
# dusman3.print()



# #inheritance
# class Calisan():
# 	def __init__(self,isim,maas,departman):
# 		print(("Calisan sinifin constructor fonksyonu"))
# 		self.isim=isim
# 		self.maas=maas
# 		self.departman=departman
# 	def goster(self):
# 		print("Calisan sinifinin bilgileri gosteriliyor...")
# 		print("Isim:",self.isim,"\nMaas:",self.maas,"\nDepartman:",self.departman)
# 	def maasazamyap(self,zammiktari):
# 		print("Maasa zam geldi")
# 		self.maas+=zammiktari
# 	def departmandegistir(self,yenidepartman):
# 		print("Departman degistiriliyor")
# 		self.departman=yenidepartman

# calisan=Calisan("Mehmet Baltaci",2500,"Insan kaynaklari")
# calisan.goster()

# class Yonetici(Calisan):
# 	def __init__(self,isim,maas,departman,kisisayi):
# 		print("yonetici classin constructor metodu ")
# 		# self.isim=isim
# 		# self.maas=maas
# 		# self.departman=departman
# 		super().__init__(isim,maas,departman)
# 		self.kisisayi=kisisayi#elave olaraq
# 		super().goster()
# 	def goster(self):
# 		print("yonetici classin bilgileri gosteriliyor")
# 		print("Isim:",self.isim,"\nMaas:",self.maas,"\nDepartman:",self.departman,"Kisisayi:",self.kisisayi)

# # yonetici.goster()
# 	def kisisayiartir(self,artir):
# 		print("Kisisayi artiriliyor..")
# 		self.kisisayi+=artir

# yonetici=Yonetici("Mehmet Baltaci",2500,"Insan kaynaklari",20)
# yonetici.kisisayiartir(15)
# yonetici.goster()
		

# class Footballer:
# 	foot_club="barcelona"
# 	age=30
# f1=Footballer()
# print(f1)
# print(f1.foot_club)
# print(f1.age)
# f1.foot_club="real madrid"
# print(f1.foot_club)



# class Square(object):
# 	edge=5
# 	area=0
# 	def area1(self):
# 		self.area=self.edge*self.edge
# 		print("Area:",self.area)
		

# s1=Square()
# print(s1)
# print(s1.edge)
# s1.area
# print(s1.area1())
# s1.edge=7
# s1.area1()


# # method vs function
# class Emp(object):
# 	age=25
# 	salary=1000 #$

# 	def ASratio(self): #method
# 		a=self.age/self.salary
# 		print("method",a)

# def ASratio(age,salary):#function,classla hec bir elaqesi yoxdur
# 	a=age/salary
# 	print("function",a)
# 	return a

# e1=Emp()
# e1.ASratio()
# # -----------------------------------------------------------------------------
# x=ASratio(22,1200)
# # print(ASratio(22,1200))
# print(x)


# # initializer or constructor
# class Animal(object	):
# 	def __init__(self,a,b):
# 		self.name=a
# 		self.age=b
# 		def getage(self):
# 			return self.age
# 		def getName(self):
# 			print(self.name)
# a1=Animal("dog",2) 
# a2=Animal("cat",3)
# a1.getName()



# "Simple Claculator"
# class Calc():
# 	"init method"

# 	def __init__(self,a,b):

# 		"initialize values"
# 		"attribute"

# 		self.value1=a
# 		self.value2=b

# 	def add(self):
# 		return self.value1+self.value2

# 	def multiply(self):
# 		return self.value1*self.value2

# 	def division(self):
# 		return self.value1/self.value2

# 	def difference(self):
# 		return self.value1-self.value2


# print("Choose: 1--add , 2--multiply , 3--division or 4--difference")
# select=int(input("select: 1,2,3,4    :::"))
# if select!=1 and select!=2 and select!=3 and select!=4:
# 	print("ERROR")
	

# v1=int(input("first value  ::"))
# v2=int(input("second value  ::"))
# c=Calc(v1,v2)
# if select==1:
# 	print("Add : {}".format(c.add()))
# elif select==2:
# 	print("Multiply : {}".format(c.multiply()))
# elif select==3:
# 	print("Division : {}".format(c.division()))
# elif select==4:
# 	print("Difference : {}".format(c.difference()))
# else:
# 	print("Error: number not found")

# # Encapsulation
# class Bankaccount(object):
# 	def __init__(self,name,money,address):
# 		self.name=name  #"-------global,public"
# 		self.__money=money  #"-------private ,amma xeta verecek,cunku melumati almaq olmayacaq,ona gore de GET ve SET metodlarindan istifade olunur"
# 		self.address=address

# 	def getMoney(self):
# 		return self.__money
# 	def setMoney(self,amount):
# 		self.__money=amount
# 	def __increase(self):
# 		self.__money=self.__money+500


# p1=Bankaccount("messi",1000,"barcelona")
# p2=Bankaccount("neymar",2000,"paris")
# print("get method: ",p1.getMoney())
# p1.setMoney(3000)
# print("after set method: ",p1.getMoney())
# p1.__increase()
# # print("after raise: ",p1.getMoney())


# # Inheritance
# # parent
# class Animal:
# 	def __init__(self):
# 		print("animal is created")
# 	def toString(self):
# 		print("animal")
# 	def walk(self):
# 		print("animal walk")

# # child
# class Monkey(Animal):
# 	def __init__(self):
# 		super().__init__() #use init of parent(animal) class 
# 		print("monkey is crated")
# 	def toString(self):
# 		print("monkey")
# 	def climb(self):
# 		print("monkey can climb")

# class Bat(Animal):
# 	def __init__(self):
# 		super().__init__()#use animal class
# 		print("bat is created")
# 	def fly(self):
# 		print("bat can fly")
# m1=Monkey()
# m1.toString()
# m1.walk()
# m1.climb()
# print("-------------------")
# b1=Bat()
# b1.walk()
# b1.fly()


# class Website:
# 	"parent"
# 	def __init__(self,name,surname):
# 		self.name=name
# 		self.surname=surname
# 	def loginfo(self):
# 		print(self.name+" "+self.surname)

# class Website1(Website):
# 	"child"
# 	def __init__(self,name, surname, ids):
# 		Website.__init__(self,name,surname)
# 		self.ids=ids
# 	def login(self):
# 		print(self.name+" "+self.surname+" "+self.ids)

# class Website2(Website):
# 	"child"
# 	def __init__(self,name,surname,email):
# 		Website.__init__(self,name,surname)
# 		self.email=email
# 	def login(self):
# 		print(self.name+" "+self.surname+" "+self.email)


# p=Website("NAME","SURNAME")
# p.loginfo()

# p1=Website1("NAME","SURNAME","123")
# p1.login()

# p2=Website2("NAME","SURNAME","email@")
# p2.login()



# # abstract
# from abc import ABC , abstractmethod
# class Animal(ABC): #super class
# 	@abstractmethod
# 	def walk(self):pass
# 	@abstractmethod
# 	def run(self):pass
# class Bird(Animal): #sub class
# 	def __init__(self):
# 		print("bird")
# 	def walk(self):
# 		print("walk")
# 	def run(self):
# 		print("run")
# # a1=Animal()
# b1=Bird()



# # overriding
# class Animal:
# 	def toString(self):
# 		print("animal")
# class Monkey(Animal):
# 	def toString(self):
# 		print("monkey")

# a1=Animal()
# a1.toString()	
# m1=Monkey()
# m1.toString()#monkey calls overriding method



"""
OOP: Object Oriented Programming
	-clas/object
	-attribitude/methods
	-encapsulation/abstration
	-inheritance
	-overriding/polymorphism
"""

# all in one
from abc import ABC, abstractmethod
#inheritance
class Shape(ABC):
	"Shape = super class/abstract class"
	# abstract method
	@abstractmethod
	def area(self):pass
	@abstractmethod
	def perimeter(self):pass
	# overriding,polymorpism
	def toString(self):pass

class Square(Shape):
	"sub class"
	def __init__(self,edge):
		self.__edge=edge #encapsulation attribute private 
	def area(self):
		result=self.__edge**2
		print("Square area:",result)
	def perimeter(self):
		result=self.__edge*4
		print("Square perimeter:",result)
	# override and polymorphism
	def toString(self):
		print("square edge:",self.__edge)

class Circle(Shape):
	"sub class"
	PI=3.14 #constant variable
	
	def __init__(self,radius):
		self.__radius=radius
	def area(self):
		result=self.PI*self.__radius**2
		print("Circle area:",result)
	def perimeter(self):
		result=2*self.__radius*self.PI
		print("Circle perimeter:",result)
	def toString(self):
		print("Circle radius:",self.__radius)

c=Circle(5)
c.area()
c.perimeter()
c.toString()
print("-----------------------------------------------")
s=Square(5)
s.area()
s.perimeter()
s.toString()
		
