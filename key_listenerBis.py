from pynput import keyboard
import time

message = "Te estas moviendo hacia "
message2 = "Te detuviste!"
direccion = "neutro"

# Esta funcion escucha el evento de presionar la tecla y printea su valor
def on_press(key):
	try:
		if key.char == 'w':
			direccion = "adelante"
			print(message,direccion)
		elif key.char == 's':
			direccion = "atras"
			print(message,direccion)
		elif key.char == 'd':
			direccion = "derecha"
			print(message,direccion)
		elif key.char == 'a':
			direccion = "izquierda"
			print(message,direccion)
		# else:
		# 	print("Solo puedes moverte utilizando w,s,d,a ")
	except AttributeError:
		print("special key {0} pressed does not do anything".format(key))
		

# Esta funcion escucha el evento de liberar la tecla y printea su valor
def on_release(key):
	direccion = "neutro"
	print(message2)
	if key == keyboard.Key.esc:
		return False

# Esta funcion escucha los eventos mientras mantenemos apretado hasta liberar y printea su valor
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
