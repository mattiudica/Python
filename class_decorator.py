class Decorador(object):
	"""Mi clase decorada"""
	def __init__(self, funcion):
		self.funcion = funcion
	def __call__(self, *args, **kwargs):
		print('Funcion ejecutada ', self.funcion.__name__)
		self.funcion(*args, **kwargs)

@Decorador
def funcRest(n,m):
	print(n-m)

funcRest(14,7)
		

