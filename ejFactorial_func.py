def factorial(x):
	res = 1
	for i in range(2, x + 1):
		res*=i
	return res
print(factorial(6))

# fac = lambda x: x and x * fac(x - 1) or 1
# print(fac(6))