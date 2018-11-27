""""COMPRENSION DE LISTAS VIENE A REEMPLAZAR LAS FUNCIONES
MAP Y FILTER EN LAS VERSIONES MAS NUEVAS DE PYTHON"""

my_int = [1,2,3,-1,-2,-3]

run_int = [num for num in my_int if num<0]

print(my_int,run_int)

my_int2 = [1,1]

my_str = ['h','e','l','o']

run_str = [s*num for s in my_str
					for num in my_int2]
print(run_str)

