#!/usr/bin/python

#Este programa procesa los archivos CSV descargados con el programa load_data.py y los convierte en archivos json

import sys
import re
from os import listdir
import json
from os.path import isfile, join
import datetime

def print_log(text):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" "+text)

print_log('Number of arguments: '+str(len(sys.argv))+' arguments.')
print_log('Argument List: '+str(sys.argv))

#aqui escaneamos el directorio donde loaddata.py creo los archivos de las acciones
mypath = "input"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for filename in onlyfiles:
    if (re.search('txt$', filename)):
        file = open(mypath+"/"+filename, "r")
        lines = file.readlines()

        #Cada CSV tiene el nombre de la accion al que corresponde la data en la primera linea del archivo
        nemo = lines[0].strip()

        #creamos el archivo de salida donde dejaremos los datos en json
        output = open("output/output_" + nemo + ".json", "w")

        print_log("reading :"+filename)
        print_log("nemo :"+nemo)
        for line in lines[3:]:
            data = {}
            vars = line.split(';')

			#aqui parseamos las variables de cada fila en el objeto data para luego guardarlo como json
            fecha = vars[0].split(" ")[0].split("-")
            data["fecha"] = fecha[2]+"-"+fecha[1]+"-"+fecha[0]
            data["accion"] = nemo
            data["precio_inicial"] = float(vars[1].replace(",","."))
            data["precio_final"] = float(vars[4].replace(",","."))
            data["var_perc"] = round((data["precio_final"]-data["precio_inicial"])/data["precio_inicial"]*100,4)

            json.dump(data, output)
            output.write("\n")
        print_log("done!")

        output.close()
        file.close()