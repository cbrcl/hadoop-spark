## Introducción
El presente trabajo tiene por objeto realizar un ejercicio práctico de explotación de datos, particularmente utilizando herramientas relacionadas con Big Data como Hadoop y Spark.

En nuestro caso el hemos definido la siguiente situación:

La bolsa de comercio de Chile pone a disposición del público las serie de datos de las acciones transadas en bolsa para los últimos 10 años. Esta información disponible se entrega como un descargable CSV (separado por “;”) con los siguientes datos:

* Fecha: fecha de transacción
* Open: valor de apertura de la acción
* High: valor máximo alcanzado por la acción
* Low: valor mínimo alcanzado por la acción
* Close: valor de cierre de la acción
* Volume: volumen de transacciones de la acción

Resulta interesante poder analizar si existe alguna relación entre las alzas o bajas de los valores de las acciones.

## Objetivo
Generar un archivo que permita analizar las posibles relaciones entre las variaciones de las acciones a lo largo de los últimos 10 años.

## Alcance
El presente trabajo es solo exploratorio y busca servir de primer paso hacia la comprensión de las herramientas de hadoop, y es por este motivo que este trabajo llegara solo hasta generar un archivo que pueda ser posteriormente analizado y queda por tanto fuera de su alcance el análisis de los datos generados.

## Referencias

Libros en pdf:
* [Hanndbook de Hadoop](https://1drv.ms/b/s!AvDC_LMtrC3ogsFpvIZLhx1qNAbTvw)
* [Introduction To Statistical Learning With R](https://1drv.ms/b/s!AvDC_LMtrC3o5yCOq5-nCbgfStGg)
* [Learning Spark](https://1drv.ms/b/s!AvDC_LMtrC3ogsFxv8wOjIl5xbzN4g)


Sitios web con instrucciones para construcción de un cluster hadoop y spark con raspberrys:
* https://tekmarathon.com/2017/02/15/hadoop-and-spark-installation-on-raspberry-pi-3-cluster-part-1/
* https://www.packtpub.com/books/content/creating-supercomputer
* https://developer.ibm.com/recipes/tutorials/building-a-hadoop-cluster-with-raspberry-pi/
* http://makezine.com/projects/build-a-compact-4-node-raspberry-pi-cluster/


Sitio web con códigos de ejemplo para correr spark con python
* https://github.com/apache/spark/blob/master/examples/src/main/python/pi.py

Sitio web con ayuda para leer json en pyspark
* https://docs.databricks.com/spark/latest/data-sources/read-json.html

Sitio web con documentación del módulo pyspark.sql
* http://spark.apache.org/docs/latest/api/python/pyspark.sql.html

Sitio web con tutorial de pyspark
* https://github.com/mahmoudparsian/pyspark-tutorial
