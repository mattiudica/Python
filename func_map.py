#---ITERACIONES DE ORDEN SUP/MAP PYTHON 2---
# def operation(n,m):
# 	if n == None or m == None:
# 		return 0
# 	return n + m

# listA = [1,2,3]
# tupB = (9,8,7)
# lr = map(operation,listA,tupB)

# print (listA)
# print(tupB)
# print(list(lr))

#--FUNC MAP CON LAMBDA PYTHON 3-----

# def double (x):
# 	return x*2
# def add (x,y):
# 	return x+y
# def product(x,y,z):
# 	return x *y*z
#---Es lo mismo que:

#Por lo general se usan func lambda cuando esa funcion va a retornar o tomar otra funcion como argumento.
# double = lambda x: x*2
# add = lambda x,y: x+y
# product = lambda x,y,z: x*y*z

# print (product(10,2,0)+add(7,7)-double(0.5))

a = [1,2,3]
b = (9,8,7)

operation = map(lambda m,n:m+n,a,b)

print (a)
print(b)
print(list(operation))  				#Para poder visualizar los resultados en una lista es necesario aplicar metodo list().
										#Sino print(operation) solo devolvera la posicion de esa funcion y no los valores que contiene.
