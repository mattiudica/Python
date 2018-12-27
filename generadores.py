#COMPRENSION DE LISTAS
# my_int2 = [1,2]

# my_str = ['h','e','l','o']

# run_str = [s*num for s in my_str
# 					for num in my_int2]
# print(run_str)

#TRANSFORMAR EN GENERADOR
# my_int2 = [1,1]

# my_str = ['h','e','l','o']

# run_str = (s*num for s in my_str
# 					for num in my_int2)						#Cambie [] por ()
# print(run_str.next())										#.next() para acceder a cada valor del siguiente paso del generador.
															#Sin el .next() retorna la ubicacion del generador unicamente.

#Para evitar poner .next por cada paso podemos hacer lo siguiente
# my_int2 = [1,2]

# my_str = ['h','e','l','o']

# run_str = (s*num for s in my_str
# 					for num in my_int2)

# for letra in run_str:
# 	print(letra)

#Esta es otra opcion, transformando una funcion normal a un objeto generador mediante el algoritmo
#Donde a diferencia del ejemplo anterior, podemos hacerlo mas complejo que un simple bucle.
#A diferencia de devolver una lista esto devuelve un conjunto de elementos iterables
#Con el yield va pausando y devolviendo los valores de cada ciclo y ejecuta el next para volver a entrar mientras la condicion se cumpla.
def factorial(n):
	i = 1
	while n>0:					#Como abajo ya multiplico i*1 si dejo asi la condicion while i*1 se hace dos veces por eso retorna dos veces 120 al final							
		i = n*i 				#Para evitarlo simplemente pongo la condicion while n>1.
		yield i
		n -= 1

for number in factorial(5):
	print(number)

