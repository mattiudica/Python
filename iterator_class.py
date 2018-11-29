# a = [1, 2, 3, 4, 5, 6, 7]

# print(dir(a)) para averiguar todos los metodos disponibles para a[]

# it = iter(a)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#exeption stop iteration, se paso el len de la lista.


# __iter__() y __next__() metodos especiales de un iterable
class listIter:

	def __init__(self, iterable):
		self.__iterable = iterable
		self.__index = -1

	def __iter__(self):
		return self
# Paso*1, con el if: agrego el raise Stop asi no rompe.
	def __next__(self):
		self.__index += 1
		if self.__index == len(self.__iterable):
			raise StopIteration
		
		return self.__iterable[self.__index]

b = [1, 2, 3, 6, 5, 4]

myList = listIter(b)

iterator = iter(myList)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# De este modo al pasarme del len del iterable no tengo la exeption stop iterarion, sino que rompe.
# Para que no tire error agregue el paso*1 en la class.

# Simplificar todos los next() con un for:
for value in iterator:
	print(value)








