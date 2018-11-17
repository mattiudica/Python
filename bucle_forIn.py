#FOR IN

listA = []
listB = []

a = 5
b = 10
c = 15

ops = [a+b,
 		b+a,
		a+c,
		c-a,
		b+c,
		c-b,
	]

for num in ops:
	#while len(ops) > 0:

	if num < 15:
		listA.append(num)
		#ops.remove(num)
	else:
		listB.append(num)
		#ops.remove(num)

print (ops,listA,listB)

#VER LA MANERA DE AL ITERAR OPS VAYA BORRANDO DE ESA LISTA LOS ELEMENTOS QUE VA AGREGANDO A LAS OTRAS DOS,
#DE MODO QUE QUEDE OPS VACIA Y LAS OTRAS DOS CON LOS VALORES DIVIDIDOS EN MAYORES O MENORES A 15


