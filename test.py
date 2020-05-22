x=1,2,3,4
print(min(x)+max(x))

y=1,2,3,4

for i in y:
	i+1
	print(i)



a=6, 7.5, 2.1, 2.0, 0, -3
print(min(a)*2)


b=6, -7.5, 2.1, -2.0, 0
for i in b:
	if i<0:
		print(i)



print(5, 0, -7, 2 ,sep='\n')

#904

s=1,2,3,-4
for i in s:
	if i>0:
		i+=2
	else:
		i
	print(i,end=',')
	

#907
z=6,7.5, 2.1, 2.0, 0

	 
#910
e=5.2,-2, 4
f=0
for i in e:
	if i>0:
		f+=i
		print(f/(len(e)-1))
	else:
		None

v=-76.45, 7.5, -5.1, 75.23
for i in v:
	abs