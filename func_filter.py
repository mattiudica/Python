#---ITERACIONES DE ORDEN SUP/FILTER PYTHON 2---
# def filtA(elem):
# 	return (elem>0)
# lA = [1,-2,3,-4,5,-6]

# lR = filter(filtA,lA)

# print (list(lR))

#---FUNC FILTER CON LAMBDA EN PYTHON 3---
#A dif de la func map, filter solo toma funciones que devuelvan un booleano(True,False).
# lB = [1,-2,3,-4,5,-6]
# lC = [7,-8,9,-10,0,-1]
# filtB = filter(lambda x: x>0,lB)
# filtC = filter(lambda y: True if y >= 0 else False,lC)

# print(lB)
# print(list(filtB))
# print(lC)
# print(list(filtC))

#---EJERCICIO PARA FILTER---
it1 = [1,-2,3,-4,0]
it2 = [5,-6,7,-8,9]
emptyListA = []
emptyListB = []

runAdd = map(lambda x,y: x+y,it1,it2)
runSub = map(lambda x,y: x-y,it1,it2)

result1=list(runAdd)+list(runSub)

emptyListA = list(filter(lambda y: True if y >= 0 else False,result1))
emptyListB = list(filter(lambda y: True if y <0 else False,result1))
result1.clear()

print(result1,emptyListA,emptyListB)