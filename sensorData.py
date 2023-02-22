import time
import json
import random
import nclib

# Configuramos el servidor y el puerto al que nos conectaremos
HOST = 'localhost'
PORT = 9999

# Creamos un objeto nclib para la conexión
nc = nclib.Netcat(listen=(HOST, PORT), verbose=True)

# Generamos datos simulados de sensores y los enviamos a través del socket
while True:
    # Generamos un valor aleatorio para la calidad del aire
    air_quality = random.choice(['good', 'moderate', 'unhealthy', 'hazardous'])
    print(air_quality)

    # Generamos un objeto JSON con los datos del sensor
    sensor_data = {'sensor_id': 1, 'quality': air_quality, 'value': random.uniform(0, 1)}

    # Enviamos los datos al servidor
    nc.send_line(json.dumps(sensor_data).encode('utf-8'))

    # Esperamos un segundo antes de enviar el siguiente conjunto de datos
    time.sleep(1)

