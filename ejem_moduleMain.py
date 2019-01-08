# Son formas de ordenar nuestros archivos/unidades de proyectos mas extensos
# Hay un modulo main o pcpal que es donde compilamos o importamos los demas modulos.
# Los distintos modulos deben estar en la misma carpeta que el modulo main, a diferencia de los paquetes.

# import ejem_moduleOther
# c= ejem_moduleOther.Ejemplo()
# c.imprime()
# ejem_moduleOther.funcEjemplo()

# Tambien podemos importar especificamente algunos valores y no todo el espacio de nombres del modulo, este caso no debo poner el nombre del modulo, puedo ejecutar directamente lo que llame:
from ejem_moduleOther import Ejemplo

e=Ejemplo()
e.imprime()

# De esta manera importo todo lo que contiene el modulo para utilizar en el main aunque no es lo recomendado ya que no visualizo facilemente de que modulo importo y genera confusion:
from ejem_moduleOther import *

e Ejemplo()

funcEjemplo()
