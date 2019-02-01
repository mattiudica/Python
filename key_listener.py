from pynput import keyboard
# Esta funcion escucha el evento de presionar la tecla y printea su valor
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

# Esta funcion escucha el evento de liberar la tecla y printea su valor
def on_release(key):
    print('{0} released'.format(key))
    # Presionando esc podemos parar el listener
    if key == keyboard.Key.esc:
        return False

# Esta funcion escucha los eventos mientras mantenemos apretado hasta liberar y printea su valor
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

