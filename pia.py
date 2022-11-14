#! python3

######
from QR import qr
#from Franco import ProgT
from Luis import luis
from Diego import mail
from wsteganew import encrip_im
import sys
import argparse
import ProgT
from Correo import enviodecorreos
######

###------------------Argumentos------------------###
parser = argparse.ArgumentParser() 
parser.add_argument("-tool", dest="nombre", help="Mencionar el nombre del script")

###------------------Argumentos wsteganew------------------### ##Se ocupan los parámetros del script a llamar para que los reconozca
parser.add_argument("-encriptar", dest="im1", help="Imagen a codificar")
parser.add_argument("-msg", dest="msgc", help="Mensaje a cifrar")
parser.add_argument("-desencriptar", dest="im2", help="Imagen a decodificar")
parser.add_argument("-key", dest="ke1", help="Llave para descifrar")
parser.add_argument("-nf", dest="ffiles", help="Nombre de la img resultante")
parser.add_argument("-nd", dest="dfiles", help="Nombre del texto descifrado")

###------------------Argumentos QR------------------###
parser.add_argument("-encode", dest="txt", help="Ingrese la ruta del txt con las urls")
parser.add_argument("-decode", dest="imgs", help="Ingrese la ruta de las imagenes")

args = parser.parse_args()


## Scripts ##
if  sys.argv[1] == "-tool":
	if sys.argv[2] == "encrip im": 
		encrip_im.main()
	if sys.argv[2] == "actualizador":
		ProgT.main()
	if sys.argv[2] == "mail":
		mail.main()
	if sys.argv[2] == "luis":
		luis.main()
	if sys.argv[2] == "qr":
		qr.main()
