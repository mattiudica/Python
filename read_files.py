f = open('ej_write.txt','w')
f.write('Hola! Estoy creando mi primer archivo write :)')
f = open('ej_write.txt','a')
f.write('. Tambien puedo agregar texto con el metodo a!  ')

# agregar = (' /agregando ','tupla ','al documento :P')
# f = open('ej_write.txt','w')
# f.seek(0,2)
# f.writelines(agregar)
print(f)
f.close()
if f.closed:
	print("El archivo se cerro y no se puede modificar hasta abrirlo nuevamente.")


# El metodo .seek() permite reemplazar y agregar texto nuevo en una posicion
# determinada por el numero que pasamos como parametro.
# Al hacerle un print al metodo .tell() podemos averiguar donde esta ubicado nuestro puntero
# pero trabajando en windows puede regresar un valor incorrecto*
# Con el metodo .writelines() podemos insertar una secuencia ej tupla o lista.

