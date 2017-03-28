#!/usr/bin/python
#Este archivo procesa los archivos json ya procesados por el programa process_data.py y los une por fechas

import re
from os import listdir
import json
from os.path import isfile, join
import datetime
import sys
import os
from shutil import copyfile


def print_log(text):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" "+text)


print_log('Number of arguments: '+str(len(sys.argv))+' arguments.')
print_log('Argument List: '+str(sys.argv))

mypath = "output/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and re.search('^output', f) and re.search('json$', f)]

#version definitiva de escritura
output_filename = "stocks.json"
#version para lectura temporal
output_filename2 = "stocks_tmp.json"
fileIndex=1;
for filename in onlyfiles[1:]:
    #Si es el primer archivo en ser procesado, el filename0 sera el del archivo en el index 0
    if (fileIndex == 1):
        filename0 = onlyfiles[0]
    #Si ya es el 2do, 3ro o n-esimo  el archivo base de lectura sera una copia del output
    else:
        print_log("Copying "+mypath + output_filename+"\t to \t"+mypath + output_filename2)
        copyfile(mypath + output_filename, mypath + output_filename2)
        filename0 = output_filename2

    #Aqui se abre el puntero al archivo de escritura
    output = open(mypath + output_filename, "w")

    # Aqui se define que el archivo a unir es el actual archivo en el arreglo
    filename1 = filename

    print_log("Joining: " + filename0 + "\t" + filename1)

    file0 = open(mypath + filename0, "r")
    lines0 = file0.readlines()

    rowIndexFile0 = 0
    for line0 in lines0[0:]:
        data0 = json.loads(line0)

        file1 = open(mypath + filename1, "r")
        lines1 = file1.readlines()
        data1 = json.loads(lines1[rowIndexFile0])

        if (data1['fecha'] == data0['fecha']):
            data2 = {}
            data2['fecha'] = data0['fecha']

            if ('acciones' in data0):
                data2['acciones'] = data0['acciones']
            else:
                data2['acciones'] = {}

            if ('accion' in data0):
                data2['acciones'][data0['accion']] = data0

            data2['acciones'][data1['accion']] = data1

            json.dump(data2, output)
            output.write("\n")

        rowIndexFile0 = rowIndexFile0 + 1

    file0.close()
    file1.close()

    output.close()
    fileIndex = fileIndex + 1

os.remove(mypath + output_filename2)