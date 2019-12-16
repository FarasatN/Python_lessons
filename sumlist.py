items = input().split()
def sum_list(items):
	sum_numbers=0
	for x in items:
		sum_numbers += int(x)
	return sum_numbers
print(sum_list(items))
