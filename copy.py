def x(n):
	for i in n:
		if i%5==0:
			print(i)
x([1,2,5,3,25,15])			



def x(n):
	for i in n:
		v=i**-1
		print(v)
	print(i==v)
x([6,7,8])


for i in range(10):
    print(str(i) * i)

x=[2,3,4,5]
y={1:'a',2:'b',3:2}
for i in x:
	if i in y:
		x.remove(i)
		print(x)

q=['a','b','c']
print(''.join(q))
z=('s',3,2,4,5,)


f={'a':2,'c':3}
for i in f:
	print(f['a'])

x={}
x['a']=1
print(x)


c=['ddrf','erfrfff']
d={i:len(i) for i in c}
print(d)
print(d.items())


def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)
