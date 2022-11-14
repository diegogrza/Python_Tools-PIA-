#! python3

######
import os
import argparse
import sys
import qrcode
import requests
import time
import json
import shutil
import qrcode
from pyzbar import pyzbar
from PIL import Image
import logging
######


#---------------##RUTAS##---------------#
def rutas():
	dir = os.path.dirname(__file__)
	global dap
	dirap = os.path.join(dir,"APIKEY") ##Es la carpeta que contendrá la apikey para poder usar virustotal
	dap = dirap+"\Akey.txt" ##Así se debe de llamar el txt con la apikey, se puede cambiar si se requiere
	global apikey
	w = open(dap,"r")
	for p in w:
		apikey=p
	global dim
	dim = os.path.join(dir,"QRs") ##Es la carpeta en la que se generaran los QRs que se requieran
	global durl
	durl = os.path.join(dir,"URLS") ##La carpeta en la que estarán los txts con la ruta de los qrs a analizar y también de los links que se quieran hacer qr
	durl = durl+"\wrlgen.txt" ##El txt con los links que se van a analizar
	global dre1
	global dre2
	dres = os.path.join(dir,"RESULTS")
	dre1 = dres+'\Sin resultados.txt' 
	dre2 = dres+'\wrls limpias.txt'
	dre3 = dres+'\wrls maliciosas.txt'
rutas()

def main():
	#---------------# ARGUMENTOS #---------------#
	parser = argparse.ArgumentParser()
	parser.add_argument("-encode", dest="txt", help="Ingrese la ruta del txt con las urls")
	parser.add_argument("-decode", dest="imgs", help="Ingrese la ruta de las imagenes")
	parser.add_argument("-tool", dest="nombre", help="Mencionar el nombre del script")
	args = parser.parse_args()
	#try:
	#	if sys.argv[3] == "":
	#		pass
	#except:
	#	print("\n[+] Ejecucion:  py qr_jorge.py -h")
	
	#---------------Logging---------------#
	logging.basicConfig(filename='app.log', level ='DEBUG')
	#---------------Registro de diagnóstico---------------#
	logging.debug("En la ruta ya se encuentra una imagen con el mismo nombre")
	logging.error("No se encontró un archivo con ese nombre en la ruta especificada")

	#---------------GENERAR QR---------------#
	if sys.argv[3] == "-encode":
		u = args.txt
		print(u)
		f = open(u,"r") 
		i=1
		for x in f:
			print("url: " + x)
			qr = qrcode.QRCode(5,error_correction=qrcode.constants.ERROR_CORRECT_L)
			url = x
			qr.add_data(url)
			qr.make()
			im = qr.make_image()
			i1 = str(i)
			name = "qr" + i1 + ".jpg"
			print(name)
			im.save(name)
			shutil.move(name, dim)
			i+=1
		f.close


	##---------------##EXTRAER LINK DE QRS Y ANALIZAR##---------------##
	elif sys.argv[3] == "-decode":
		pa = args.imgs
		a = open(pa,"r")
		arc = open(durl, "w")
		for s in a:
			print("nombre de qr: " + s)
			s = s.rstrip()
			image = Image.open(s)
			qr_code = pyzbar.decode(image)[0]
			data= qr_code.data.decode('utf8').encode('shift-jis').decode('utf-8')
			print("El mensaje es: ",data)
			arc.write(data)
		arc.close()
		a.close()
		#FIN EXTRAER LINK QR

		#HACER EL REPORTE
		url = 'https://www.virustotal.com/vtapi/v2/url/report'
		ars = open(durl,"r")
		parameters = {'apikey': apikey, 'resource': ars}

		for i in ars:
			parameters = {'apikey': apikey, 'resource': i}
			response= requests.get(url=url, params=parameters)
			json_response= json.loads(response.text)

			if json_response['response_code'] <= 0:
				with open(dre1, 'a')  as notfound:
					notfound.write(i) and notfound.write("\tNo se encontró la URL\n")
			elif json_response['response_code'] >= 1:

				if json_response['positives'] <= 0:
					with open(dre2, 'a')  as clean:
						clean.write(i) and clean.write("\t No es malicioso \n")
				else:
					with open(dre3, 'a')  as malicious:
						malicious.write(i) and malicious.write("\t Malicious") and malicious.write("\t Este dominio detectó   "+ str(json_response['positives']) + "  pruebas fallidas\n")
			time.sleep(1)
		ars.close()
