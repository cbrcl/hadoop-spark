#!/usr/bin/python
#Este programa se conecta a la pagina de la bolsa de santiago consulta por las acciones entregadas
#como parametros para descargar y crear como archivos los datos de los ultimos 10 anos

import datetime
import sys

#Para python 2.7 se utiliza esta libreria
import urllib2

#Para python 3.x se utiliza otra libreria para la conexion con el sitio web, 
#es por este motivo que se debe descomentar la siguiente linea 
#from urllib.request import urlopen

#Definimos una funcion que nos permite extraer la informacion desde la url 
def load_data(nemo):
    #definimos el path donde guardaremos los archivos descargados de la pagina de la bolsa de santiago
    path = "input/"
    #creamos el nombre del archivo con el que guardaremos los datos de la accion solicitada
    filename = nemo + ".txt"
    #creamos la url desde la que descargaremos los datos
    url = "http://www.bolsadesantiago.com/mercado/Paginas/Resumen-de-Instrumento.aspx?RequestHistorico=1&Nemo=" + nemo

    print_log("reading " + nemo + " data from: "+url)
    
    #creamos un objeto de conexion a la url
    response = urllib2.urlopen(url)
    
    #realizamos la conexion a la url y leemos los datos que nos entrega, limiando los caracteres \x00
    #python 2.7
    html = response.read()
    my_file = html.replace("\x00","")
	
	#python 3.x
	#html = urlopen(url)
    #my_file = html.read().decode('utf-8').replace("\x00","")
	
    print_log("finished reading!")
    
    print_log("writing file: " + filename)
    
    #creamos el archivo de destino donde almacenaremos la informacion descargada
    text_file = open(path+filename, "w")
    text_file.write(my_file)
    text_file.close()

    print_log("done!")


def print_log(text):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" "+text)


print_log('Number of arguments: '+str(len(sys.argv))+' arguments.')
print_log('Argument List: '+str(sys.argv))

#para cada uno de las acciones entregadas como parametros, realizamos la extraccion de los datos
#ejemplo de como ejecutar este programa:
#python load_data.py LAN COPEC CAP SQM-B
for index in range(1, len(sys.argv)):
    nemo = sys.argv[index]
    load_data(nemo)
