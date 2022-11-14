#! python3

###
import subprocess, sys
import logging
###

def main():
	#---------------Logging---------------#
	logging.basicConfig(filename='app.log', level ='DEBUG')
	#---------------Registro de diagnóstico---------------#
	logging.error("Ya existe esta tarea ejecutandose, borrala desde el programador de tareas")
	
	#---------------SCRIPT---------------#
	h = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "Programador.ps1"', stdout=sys.stdout)
	h.communicate()