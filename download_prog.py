from PIL import Image
import os
import random
import requests

# Revisar donde incorporar el manejo de excepciones para que funcione realmente, y no descargue archivos vacios
# por error en tipeo de url o demas errores.
try:
	get = str(input("Enter url of image for download : "))

	def download_img(url):
		print("DOWNLOADING...")
		name = random.randrange(1,1000)
		full_name = str(name) + ".jpg"
		r = requests.get(url, stream = True)

		with open(full_name, 'wb') as f:
			f.write(r.content)
		return "DOWNLOAD COMPLETED. SAVED AS : " + full_name
		
except:
	print("Ups, something went wrong :(")
	exit()
else:
	print(download_img(get))

	

