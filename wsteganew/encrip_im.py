#! python3

#####
from Esteganew.esteganew import *
import argparse  
import sys
import os
import shutil
import logging
#####



def main():
	#----------------Argumentos----------------#
	parser = argparse.ArgumentParser()  
	parser.add_argument("-encriptar", dest="im1", help="Imagen a codificar")
	parser.add_argument("-msg", dest="msgc", help="Mensaje a cifrar")
	parser.add_argument("-desencriptar", dest="im2", help="Imagen a decodificar")
	parser.add_argument("-key", dest="ke1", help="Llave para descifrar")
	parser.add_argument("-nf", dest="ffiles", help="Nombre de la img resultante")
	parser.add_argument("-nd", dest="dfiles", help="Nombre del texto descifrado")
	parser.add_argument("-tool", dest="nombre", help="Mencionar el nombre del script")
	args = parser.parse_args()
	

	#---------------Logging---------------#
	logging.basicConfig(filename='app.log', level ='DEBUG')
	#---------------Registro de diagnóstico---------------#
	logging.debug("En la ruta ya se encuentra un archivo con el mismo nombre")
	logging.error("No se encontró un archivo con ese nombre en la ruta especificada")


	#----------------Codificar----------------#
	if sys.argv[3] == "-encriptar":
		mensaje = enCRYptar(args.msgc)
		dir = os.path.dirname(__file__)
		d2 = os.path.join(dir,"extraer")
		imag_cod = Esteganew(args.im1,mensaje,args.ffiles)
		imag_cod.codificar()
		nm = args.ffiles + ".png"
		shutil.move(nm,d2) # Siempre que quieras cifrar un msj en la imagen tendrás que borrar tanto la key como la imagen con el msj cifrado de la carpeta extraer para evitar errores
		shutil.move("miLlave.key",d2)


	#----------------Decodificar----------------#
	elif sys.argv[3] == "-desencriptar":
		imag_dec = Esteganew(args.im2) # Los argumentos de la imagen y la key deberán ser la ruta completa 
		archivo_clave = "miLlave.key"
		mensaje_pre = imag_dec.decodificar()
		mensaje_post = deCRYptar(mensaje_pre,args.ke1)
		while True:
			nombre_archivo = args.dfiles
			break
		dir = os.path.dirname(__file__)
		d1 = os.path.join(dir,"extraer")
		d4 = '\\'
		d1 =  d1+ d4 + args.dfiles
		archivo = open(d1, "w")
		archivo.write(mensaje_post)
		archivo.close()