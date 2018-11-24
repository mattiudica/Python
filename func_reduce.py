#---ITERACIONES DE ORDEN SUP/REDUCE SIN LAMBDA---
from functools import reduce

iter1 = ["Hola", "mundo", "desde", "Python"]
iter2 = (3,15,25)
def add_str_int(a,b):
 if type(a) and type(b) == str :
 	return " ".join((a, b)).lower()
 elif type(a) and type(b) == int :
 	return a+b

rr = reduce(add_str_int, iter2)
print(type(rr))
print(rr)

#---FUNC REDUCE CON LAMBDA EN PYTHON 3---
abcList = ('A','B','C')
funcRed = reduce(lambda x,y : x + y,abcList)
print(type(funcRed))
print(funcRed.lower())
