# Cuando abrimos un archivo se crea un objeto de tipo file.
# f = open() recibe tres parametros los cuales dos son opcionales, el primero es el archivo/ruta, el segundo
# el modo de acceso y el tercero tamaño de woofer(?). Al finalizar de abrir y manipular el archivo se debe
# cerrarlo f.close().

# Modo de acceso read, si no colocamos ninguno por defecto se selecciona read.
# try:
# 	f = open('ej_open.txt','r')
# except:
# 	print('El archivo ingresado no existe.')
# else:
# 	print(f)

# Modo write, si no existe el file lo crea, si existe borra el contenido y lo reemplaza:
# f = open('ej_open.txt','w')
# print(f)
# f.close()

# Modo read+write:
# try:
# 	f = open('ej_open.txt','r+')
# except:
# 	f='error'
# 	print('El archivo ingresado no existe.')
# else:
# 	print(f)
# f.close()

# Modo append, debe existir el archivo y agrega nuevo contenido al final en vez de reemplazar como 'w':
# try:
# 	f = open('ej_open.txt','a')
# except:
# 	f='error'
# 	print('El archivo ingresado no existe.')
# else:
# 	print(f)
# f.close()








