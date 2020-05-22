def our_func(red,**scores):
	print({red})
	for k,v in scores.items():
		print('{}:{}'.format(k,v))
our_func('home',w=3,a='book')





mylist = [5,2,1,8,4]
n = len(mylist)
for i in range(n):
    for j in range(1, n-i):
        # swap if prev value is less than current value
        # change < to > to reverse the order
        if mylist[j-1] < mylist[j]:
            # do a tuple swap
            (mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
print(mylist)


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

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
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [5,2,1,8,4]
mergeSort(myList)
print(myList)


# Recursive Python Program for merge sort

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

# Code Contributed by Mohit Gupta_OMG 


def partition(sort_list, low, high):
    i = (low -1)
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1]
    return (i+1)
            
def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi-1)
        quick_sort(sort_list, pi+1, high)
lst = []
size = int(input("Enter size of the list: "))
for i in range(size):
    elements = int(input("Enter an element"))
    lst.append(elements)
low = 0
high = len(lst) - 1
quick_sort(lst, low, high)
print(lst)



def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

alist = [54,26,93,17,77,31,44,55,20]
print(quicksort(alist))