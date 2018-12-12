from time import time

def timing_dec(func):
	def wrap_func(*args, **kwargs):
		start = time()
		print(start)
		result = func(*args, **kwargs)
		end = time()
		print(end)
		print('Enlapsed time: {}'.format(end - start))
		return result

	return wrap_func

@timing_dec
def my_func(num):
	sum = 0
	for i in range(num+1):
		sum += i
	return sum


print(my_func(20000000))
