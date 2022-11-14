# Importamos librerías
import logging
import smtplib, ssl
import mimetypes

logging.basicConfig(filename='app.log', level= 'DEBUG')
logging.debug("No se encuentra ese archivo")
logging.error("Archivo inexistente")

# Importamos los módulos necesarios
from email.mime.multipart import MIMEMultipart

def main():
    # Creamos objeto Multipart, quien será el recipiente que enviaremos
    with open("mails.txt") as archivo:
        for linea in archivo:
      
            msg = MIMEMultipart()
            msg['From']="TU CORREO"
            msg['To']=linea      
  
# Autenticamos
            mailServer = smtplib.SMTP('smtp.gmail.com',587)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            mailServer.login("TU CORREO","TU CONTRASEÑA")

# Enviamos
            mailServer.sendmail("TU CORREO",linea, msg.as_string())

# Cerramos conexión
            mailServer.close()

