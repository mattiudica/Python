from PIL import Image
import os
# Este script recorre el directorio y capta los archivos que finalizan en '.jpg', crea un archivo por cada uno
# separando nombre y extension y luego los vuelve a guardar en otra carpeta con otra extension '.png'.
 for f in os.listdir('.'):
	if f.endswith('.jpg'):
		i = Image.open(f)
		fn, fext = os.path.splitext(f)
		i.save('PNG/{}.png'.format(fn))

# Este script abre una imagen del directorio y cambia su modo de color y tamaño.
size_300 = (300,300)
image1 = Image.open('mtg_card.jpg')
image1.convert(mode='L')
image1.thumbnail(size_300)
image1.save('mtg_cardMod_300.jpg')
image1.show()
