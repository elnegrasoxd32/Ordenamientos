import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0, 0.004550, 0.007999,0.005642, 0.008016, 0.013295,0.021159, 0.029097,0.020176, 0.023819, 0.022023, 0.032118 , 0.071996, 0.117075 , 0.153642, 0.210024, 0.252781 , 0.293793,0.240449,0.277799,0.429942 ]
tiempo_java=[0.000130, 0.000732, 0.000920, 0.001006, 0.001326, 0.001552, 0.001865, 0.002380, 0.002967, 0.003119, 0.003360, 0.007121, 0.010703, 0.012693, 0.015796, 0.019778, 0.023341, 0.026932, 0.027300, 0.032195, 0.044084]
tiempo_cpp=[0,0,0.001001,0.002202,0.02,0.003001,0.004,0.005,0.006,0.007,0.007,0.008001,0.015006,0.032591,0.043034,0.055576,0.070738,0.067515,0.090475,0.102924,0.117288]

# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='blue')
plt.plot(tamanos, tiempo_cpp, label='C++', color='orange')
plt.plot(tamanos, tiempo_java, label='Java', color='red')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (ms)')
plt.title('Tiempo de ejecución de MergeSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()