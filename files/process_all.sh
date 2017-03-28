#1er paso: Descargar archivos CSV de acciones
python load_data.py CAP LAN SQM-B COPEC

#2do paso: Convertir CSV a JSON
python process_data.py

#3er paso: Unir por fecha los archivos de las acciones
python join_by_date.py

#4to paso: Procesar archivo en spark

#Eliminar archivos previamente utilizados
hadoop fs -rm /stocks.json
hadoop fs -rm -r /stocks-result

#Copiar nuevo archivo generado a hdfs
hadoop fs -copyFromLocal output/stocks.json /stocks.json

#Procesar archivo con spark
spark-submit --master spark://hdmaster:7077 --conf spark.executor.memory=768m spark_stocks.py

#Eliminar copia local de resultados previos
rm -r -f stocks-result

#Copia desde hdfs a local de los nuevos resultados
hadoop fs -copyToLocal /stocks-result stocks-result