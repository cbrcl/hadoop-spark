# ejemplo de ejecucion
# nota: este archivo tiene escrito en duro el archivo que procesara
# spark-submit --master spark://hdmaster:7077 --conf spark.executor.memory=768m spark-stocks.py

import sys
import json

import findspark
findspark.init()

from pyspark.sql import SparkSession, SQLContext

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("Python JSON")\
        .getOrCreate()
    
    filename = "/stocks.json"
    df = spark.read.json(filename)
    
    df.registerTempTable("stocks")
    
    result = spark.sql("select 	fecha, \
		    					acciones.CAP.var_perc AS CAP, \
		    					acciones.`SQM-B`.var_perc AS SQM, \
		    					acciones.`COPEC`.var_perc AS COPEC, \
		    					acciones.`LAN`.var_perc AS LAN \
		    			from stocks")
    			
    result.show()
    
    output = "/stocks-result"
    
    result.write.save(output, format="json")