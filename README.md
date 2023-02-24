# Aplicación de monitoreo de calidad del aire en tiempo real
Esta es una aplicación que utiliza Apache Spark para procesar y analizar datos en tiempo real de sensores que monitorean la calidad del aire. La aplicación consta de dos componentes principales:

**airQ.py**: Este script de Python utiliza Spark Streaming para procesar los datos de los sensores en tiempo real y calcular la cantidad de lecturas buenas de calidad del aire.

**sensorData.py**: Este script de Python genera datos simulados de sensores y los envía a través de un socket a la aplicación airQ.py.

Requisitos previos
Antes de poder utilizar esta aplicación, necesitará tener instalado lo siguiente:

* Python 3.x
* Apache Spark
* nc (Netcat)

## Cómo lanzar la aplicación
Para lanzar esta aplicación, siga los siguientes pasos:

Clone este repositorio en su máquina local.

Abra una terminal y navegue a la carpeta raíz del repositorio.

Abra dos pestañas de la terminal.

En una pestaña, inicie la aplicación airQ.py ejecutando el siguiente comando:

```spark-submit airQ.py```

En la otra pestaña, inicie la aplicación sensorData.py ejecutando el siguiente comando:

```python sensorData.py```

Esto lanzará ambas aplicaciones y comenzará a enviar datos simulados de sensores a través de un socket a la aplicación airQ.py para su procesamiento en tiempo real. La aplicación airQ.py mostrará el número de lecturas buenas de calidad del aire en tiempo real en la consola.

Nota: 
* Asegúrese de que el servidor y el puerto en el script sensorData.py coincidan con los del script airQ.py.
* Para instalar nclib use:
```sudo apt-get install python3-pip```
```pip3 install nclib```
