def our_func(red,**scores):
	print({red})
	for k,v in scores.items():
		print('{}:{}'.format(k,v))
our_func('home',w=3,a='book')
