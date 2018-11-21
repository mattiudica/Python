class Prueba(object):
	def __init__(self):
		self.__private = 'Soy un atr privado'
		self.public = 'Soy un atr publico'
	def __metodoPrivate(self):
		return'Soy el metodo pirvado'
	def metodoPublico(self):
		return'Soy el metodo publico'

	def setPrivate(self, valor):
		#self.__private = valor						#Paso0*
		self.__private = self.__metodoPrivate() 	#Paso1*

	def getPrivate(self):
		return self.__private
	


obj = Prueba()
#print(obj.public)
#print(obj.__private)								#Al ser un atr privado no lo puedo accesar de este modo.
										
obj.setPrivate('Tengo nuevo valor')					#Tiene sentido si hago esto junto al Paso0*, entonces si retorna el valor por parametro ('Tengo nuevo valor'). Si hago el paso1* este lo pisa al parametro que le pase y queda el valor que defini en la class, es decir 'Soy el metodo privado' por lo que directamente llamo el print(obj.getPrivate()) sin el set.
print(obj.getPrivate())								#Asi si.

#print(obj.__metodoPrivate())						#Al ser un metodo privado no lo puedo accesar de este modo.
													#Los metodos priv a diferencia de los atr, solo se pueden acceder dentro de la class y luego llamarlos desde un atr como en el paso1*, no hay manera de llamarlos por fuera directamente.
print(obj.metodoPublico())
						