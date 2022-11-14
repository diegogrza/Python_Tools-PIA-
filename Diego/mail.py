#En este script, se hara webscrapping a una pagina web
#obtendremos los correos electronicos, y los guardaremos en un txt
import requests
from bs4 import BeautifulSoup as bs
import re
import os
from lxml import html
import logging

def main():
    def html_page(link_page):
        try:
            #hacemos el request
            html = requests.get(link_page)
            content = html.content
            soup = bs(content, "lxml") #guardamos el contenido html en esta variable
            html_txt = open('html.txt', 'w', encoding='utf-8')
            html_txt.write(str(soup)) #escribimos en el txt
            html_txt.close()
        except:
            print('Revisa que sea correcto el link ingresado')
            pass

    def re_mail():
        try:
            mail_reg = re.compile(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b') #regex de validor de mail
            lista_mail = [] #lista donde guardaremos los mails
            with open('html.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    buscar = re.search(mail_reg, line)
                    if buscar != None: #si cumplen con la condicion que no es NONE, significa que el mail_reg empato con un mail en el archivo
                        lista_mail.append(buscar.group()) #agregamos cada uno a la lista, le pongo grupo(),para que solo de el resultado y no otros datos inecesarios
            with open('Luis/mails.txt', 'w',encoding='utf-8') as file:
                for i in range(0,len(lista_mail)):
                    file.write(str(lista_mail[i])+'\n') #escribimos la lista en el archivo txt
                os.remove("html.txt") #eliminamos el archivo html porque ya no nos sirve
            print('Creado la lista de mails, se guardo el txt en la carpeta de /Luis')
        except:
            pass
    print('OBTEN LOS MAILS DE UNA PAGINA WEB')
    print('───▄▄▄')        
    print('─▄▀░▄░▀▄')        
    print('─█░█▄▀░█')        
    print('─█░▀▄▄▀█▄█▄▀')        
    print('▄▄█▄▄▄▄███▀')        

    link = input('Escribe el URL = ')
    html_page(link)
    re_mail()

    
#configuracion logging
    logging.basicConfig(filename='app.log', level='DEBUG')
    logging.critical('El host' + link + 'no esta disponible')
    logging.error('El host' + link +'no se encontro')
    