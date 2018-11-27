#COMPRENSION DE LISTAS
# my_int2 = [1,2]

# my_str = ['h','e','l','o']

# run_str = [s*num for s in my_str
# 					for num in my_int2]
# print(run_str)

#TRANSFORMAR EN GENERADOR
# my_int2 = [1,1]

# my_str = ['h','e','l','o']

#run_str = (s*num for s in my_str
					#for num in my_int2)						#Cambie [] por ()
#print(run_str.next())											#.next() para acceder a cada valor del siguiente paso del generador.
																#Sin el .next() retorna la ubicacion del generador unicamente.

#Para evitar poner .next por cada paso podemos hacer lo siguiente
my_int2 = [1,2]

my_str = ['h','e','l','o']

run_str = (s*num for s in my_str
					for num in my_int2)

for letra in run_str:
	print(letra)

#Esta es otra opcion, transformando una funcion normal a un objeto generador mediante el algoritmo
#Donde a diferencia del ejemplo anterior, podemos utilizar operadores y hacerlo mas complejo.



