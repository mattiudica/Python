from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

time.sleep(5)
# # keyboard.press('w')
# # keyboard.release('w')
# # keyboard.press(Key,cmd)
# # keyboard.release(Key,cmd)
keyboard.type("Hola Mundo! Estoy probando la funcion type fuera de consola :)")