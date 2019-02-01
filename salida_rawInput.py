valor1=123
valor2=' Hola Hola'
valor3=' Hola Hola Aqui concateno valores str e int de dos formas distintas'
print(valor1,valor2+valor3)
print('Hola mundo,\naqui pruebo el interlineado')
print('Hola mundo,\n\taqui pruebo el interlineado con tabulador')
print('Mi edad es',26,'y soy hombre.')
#Podemos utilizar especificadores de valor al imprimir:
edad=26
print('Mi edad es: %d años.' %edad)
print('Mi edad es: %d %s.' %(edad,'años'))
#Podemos elegir la extension a imprimir del total del valor:
humedad=80.2567709
print('La humedad en la ciudad de Buenos Aires es de: %.2f'%humedad)
#Tambien se pueden agregar espacios:
print('Aqui agrego 10 espacios a la %-10sde la sentencia.'%'derecha')
x = 50
y = 10
print('50 * 10 or x * y = ', x*y)
# Es lo mismo que hacer:
print("{0}*{1} = {2}".format(x,y,x*y))
print("Hello","fucking","world",sep=("-----------"))

# Entrada raw input
# Todo valor que reciba desde el teclado se guarda en la variable valor y se imprime
# valor = input()						
# print(valor+' es de tipo', type(valor))
# Va a ser siempre de type str a menos que lo convierta.
try:
	valor = input('Prueba el raw input ingresando cualquier valor en el teclado: ')
	valor = int(valor)
except:
	print(valor + ' es de tipo str.')
else:
	print(valor,' es de tipo int.')

