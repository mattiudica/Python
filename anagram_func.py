# funcion que tome de un input una palabra y devuelva un anagrama de esa palabra y el input original:
from functools import reduce

def anagramFunc(palabra):
	sortList = sorted(palabra, reverse=True)
	reduceAnag = reduce(lambda x,y : x + y,sortList)
	return(reduceAnag.lower())

inputStr = input("Ingresa una palabra: ")

anagReturn = anagramFunc(inputStr)

def reverse_anag():
	reverse=inputStr
	return(reverse.lower())

originalStr= reverse_anag()

print("Elegiste la palabra: ",originalStr, """
	\ny su anagrama es: """,anagReturn)
