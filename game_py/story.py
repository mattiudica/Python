from character import Character 
from weapons_armors import Item
from maze import *
import pyfiglet
import time
import winsound

winsound.PlaySound("gamemusic.wav", winsound.SND_ASYNC)

ascii_banner = pyfiglet.figlet_format("        THE\n                    SEARCH\n")
time.sleep(1)
print(ascii_banner)
time.sleep(10)
welcome = print("CREA UN PERSONAJE Y COMIENZA TU PROPIO CAMINO...\n\n")


while True:

	time.sleep(4)
	char_name = input("Dale un nombre a tu personaje:\n").lower()
	time.sleep(2)
	char_ocupation = input("Elige un camino, wizard / fighter:\n").lower()
	
	if (char_name != "") and (char_ocupation == 'fighter' or char_ocupation == 'wizard'):
		time.sleep(3)
		print("Muy bien "+char_name+" tomaste el camino del "+char_ocupation)
		break
	else:
		print("Recuerda completar todos los campos y utilizar las palabras designadas\n")

NewChar=Character(char_name,char_ocupation)
NewChar.subclassAtack()
bault ={}

time.sleep(3)
print("Para comenzar el viaje debes equiparte y conseguir oro.\nSi resuelves este acertijo, obtendras lo que necesitas para seguir viaje...\n")
time.sleep(3)
print("Entre mas grande crece menos se ve...\n")
time.sleep(3)

while True:

	acertijo0 = input("En una sola palabra ¿Que es?\n").lower()

	if (acertijo0 != "") and (acertijo0 == 'oscuridad'):
		time.sleep(2)
		print("Fantástico "+ NewChar.name +" acertaste, toma esto y continua tu camino...\n\n")
		basicWeapon=None
		basicArmor=None
		if NewChar.ocupation == 'fighter':
			basic_sword=Item('c',10,'weapon',38,'regular')
			basic_armor=Item('c',15,'armor',62,'regular')
			basic_sword.subclassStat()
			basic_armor.subclassStat()
			basicWeapon=basic_sword
			basicArmor=basic_armor
			NewChar.atack = NewChar.atack + basicWeapon.pAtack
			gold = 150
			bault["basic sword"]=basic_sword
			bault["basic armor"]=basic_armor
			bault["gold"]=gold
			time.sleep(2)
			print("Obtuviste: ", bault.keys())
		else:
			basic_staf =Item('c',10,'weapon',38,'magical')
			basic_robe=Item('c',15,'armor',55,'magical')
			basic_staf.subclassStat()
			basic_robe.subclassStat()
			basicWeapon=basic_staf
			basicArmor=basic_robe	
			NewChar.magicAtack = NewChar.magicAtack + basicWeapon.pAtack
			gold = 150
			bault["basic staf"]=basic_staf
			bault["basic robe"]=basic_robe
			bault["gold"]=gold
			time.sleep(2)
			print("Obtuviste:", bault.keys())
		break
	else:
		time.sleep(2)
		print("Eso es incorrecto! Pero intentalo una vez mas...")


NewChar.defense = NewChar.defense + basicArmor.pCover

time.sleep(3)
print("Ya estas listo para la primer mision. Viaja a la siguiente ciudad, debes pagar 50 monedas de oro\n")
shipPay = 50
bault["gold"] = bault["gold"] - shipPay
time.sleep(5)
print("Pagaste el viaje, te resta de oro:",bault["gold"])
time.sleep(3)
travel = print("\n\nviajando...")
time.sleep(2)
travel = print("viajando...")
time.sleep(2)
travel = print("viajando...")
time.sleep(2)
travel = print("viajando...\n\n")
time.sleep(3)
newChallenge=print("Bienvenido a la ciudad X!\nVamos a poner a prueba tu habilidad con un contrincante.\n\n")
time.sleep(5)
rival1 = print("CONTRINCANTE N° 1:\n-'Soy el Genio de los acertijos, me encomendaron probar tu ingenio.\nVeamos...'\n")
time.sleep(3)


acertijoLetras = ['u','d','t','c','c','s','s','o','n']
max_guesses1 = 5
guessed1 = False

for wrong1 in range(max_guesses1):
	time.sleep(3)
	acertijo1 = input("Coniderando la siguiente sueson de letras, que letra es la que sigue para que la sucesion sea coherente?... Pista: Esta se ecunetra ya en el conjunto dado\nu-d-t-c-c-s-s-o-n\n").lower()
	if acertijo1 == acertijoLetras[1]:
		guessed1 = True		
		NewChar.exp = NewChar.exp +50		
		time.sleep(1)
		print("Eso es correcto! Veamos como te va con el siguiente...\n\n")
		break
else:
  print("Superaste el maximo de {} respuestas incorrectas\n GAME OVER :(".format(max_guesses1)) 
  exit()
if not guessed1:
  wrong1 += 1

max_guesses2 = 3
guessed2 = False

for wrong2 in range(max_guesses2):
	time.sleep(3)
	acertijo2 = input(str("Dime el numero el cual el valor de su cifra es igual a la cantidad de letras que componen su nombre\n")).lower()
	if acertijo2 == '5' or acertijo2 == 'cinco':
		guessed2 = True
		NewChar.exp = NewChar.exp +50		
		time.sleep(2)
		print("Eso es correcto! Veo que estas preparado. Ganaste {} puntos de experiencia".format(NewChar.exp))
		break
else:
	time.sleep(2)
	print("Superaste el maximo de {} respuestas incorrectas\n GAME OVER :(".format(max_guesses2))
	exit()
if not guessed2:
	wrong2 += 1

print(NewChar.characterStats())
print(bault.items())
