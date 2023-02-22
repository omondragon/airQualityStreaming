from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import json

# Creamos un objeto StreamingContext con una ventana de 10 segundos
sc = SparkContext("local[*]", "QualityAir")
ssc = StreamingContext(sc, 10)

# Creamos un socket de escucha en el puerto 9999
socket_stream = ssc.socketTextStream("localhost", 9999)

# Convertimos cada línea de texto a un objeto JSON
sensor_data_stream = socket_stream.map(lambda line: json.loads(line))

# Filtramos los datos de los sensores que estén fuera del rango de calidad del aire deseado
quality_air_stream = sensor_data_stream.filter(lambda data: data['quality'] == "good")

# Contamos el número de lecturas buenas de calidad del aire
good_quality_air_count_stream = quality_air_stream.count()

# Imprimimos el resultado en tiempo real
good_quality_air_count_stream.pprint()

# Iniciamos el procesamiento en streaming
ssc.start()

# Esperamos a que la aplicación termine
ssc.awaitTermination()
