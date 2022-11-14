#! python3

#####
from datetime import datetime
import subprocess, sys
import argparse
#####


    
##Script##
Dia = datetime.today().strftime('%A') #Esta linea especifica el nombre del dia actual
Lunes = 'Monday'
Martes = 'Tuesday'
Miercoles = 'Wednesday'
Jueves = 'Thursday'
Viernes = 'Friday'
Sabado = 'Saturday'
Domingo = 'Sunday'

#Dia es igual al dia escrito , por lo que el dia escrito es el primer condicional con el que se especifica el dia o los dias a instalar las actualizaciones
if Dia == Lunes:	
	p = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "Instalador.ps1"' , stdout=sys.stdout)
	p.communicate()
	
else:
	f = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "Pr.ps1"' , stdout=sys.stdout)
	f.communicate()
