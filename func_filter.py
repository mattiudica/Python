#---ITERACIONES DE ORDEN SUP/FILTER PYTHON 2---
# def filtA(elem):
# 	return (elem>0)
# lA = [1,-2,3,-4,5,-6]

# lR = filter(filtA,lA)

# print (list(lR))

#---FUNC FILTER CON LAMBDA EN PYTHON 3---
#A dif de la func map, filter solo toma funciones que devuelvan un booleano(True,False).
lB = [1,-2,3,-4,5,-6]
lC = [7,-8,9,-10,0,-1]
filtB = filter(lambda x: x>0,lB)
filtC = filter(lambda y: True if y >= 0 else False,lC)

print(lB)
print(list(filtB))
print(lC)
print(list(filtC))

#---EJERCICIO PARA FILTER---
# listA = []
# listB = []

# a = 5
# b = 10
# c = 15
# d = 20

# ops = [a+b,
#  		b+a,
# 		a+c,
# 		c-a,
# 		b+c,
# 		c-b,
# 	]

# for num in ops:
# 	#while len(ops) > 0:

# 	if num < 15:
# 		listA.append(num)
# 		#ops.remove(num)
# 	else:
# 		listB.append(num)
# 		#ops.remove(num)

# print (ops,listA,listB)

