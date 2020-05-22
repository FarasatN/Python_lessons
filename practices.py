def bubble_sort(n):
	s=True
	while s:
		s=False
		for i in range(len(n)-1):
			if n[i]>n[i+1]:
				n[i],n[i+1]=n[i+1],n[i]
				s=True
n=[5,2,1,8,4]
bubble_sort(n)
print(n)


l = [5,2,1,8,4]
nl = []
while l:
    m = l[0]  # arbitrary number in list 
    for x in l: 
        if x < m:
            m = x
    nl.append(m)
    l.remove(m)    
print(nl)



def mergeSort(ml):
    if len(ml) > 1:
        mid = len(ml) // 2
        left = ml[:mid]
        right = ml[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              ml[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                ml[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            ml[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            ml[k]=right[j]
            j += 1
            k += 1

ml = [5,2,1,8,4]
mergeSort(ml)
print(ml)



def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break

	return result

def mergesort(list):
	if len(list) < 2:
		return list

	middle = len(list)//2
	left = mergesort(list[:middle])
	right = mergesort(list[middle:])

	return merge(left, right)
	
seq = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(seq); 
print("\n")
print("Sorted array is")
print(mergesort(seq))



l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print(l)





def sort(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index-1
        while i>=0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i -= 1
            else:
                break
list[5,2,1,8,4]
print(sort(list))


data = [3, 1, 5, 2, 4]
n = len(data)
for i in range(n):
    for j in range(1,n):
        if data[j-1] > data[j]:
            (data[j-1], data[j]) = (data[j], data[j-1])
		print(data)



def asc(a):
	b=[]
	l=len(a)
	for i in range(l):
		x=min(a)
		b.append(x)
		a.remove(x)
		    return b
print asc([2,5,8,7,44,54,23])


# Your current setup
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list  = []
# Sort function
for i in data_list:
    new_list = [ x for x in new_list if i > x ] + [i] + [ x for x in new_list if i <= x ]
prit(new_list)





s = [-5, -23, 5, 0, 23, -6, 23, 67]
nl = []
for i in range(len(s)):
    a = min(s)
    nl.append(a)
    s.remove(a)

print nl


a = [3, 1, 5, 2, 4]

for i in a[1:]:
    j = a.index(i)
    while j > 0 and a[j-1] > a[j]:
        a[j], a[j-1] = a[j-1], a[j]
        j = j - 1
print()


mylist = [1, 6, 7, 8, 1, 10, 15, 9]
print(mylist)
n = len(mylist)
for i in range(n):
    for j in range(1, n-i):
        if mylist[j-1] > mylist[j]:
             (mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
print(mylist)

