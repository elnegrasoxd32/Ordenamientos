import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0, 0.003531, 0.000000,0, 0, 0, 0.002051, 0.000000, 0.004521, 0, 0.003520, 0.008029, 0.003012, 0.020983, 0.019658, 0.019328, 0.031728, 0.024971, 0.032568, 0.029566, 0.050189]
tiempo_cpp = [0, 0,0,0,0,0,0,0,0,0.001001,0,0,0,0.001001,0.001,0.000999,0.001,0.002307,0.000999,0.00203,0.003012]
tiempo_java=[0.000022, 0.000149, 0.000184, 0.000199, 0.000211, 0.000252, 0.000311, 0.000322, 0.000360, 0.000928, 0.001001, 0.002236, 0.002413, 0.003236, 0.003280, 0.004505, 0.005064, 0.005086, 0.006692, 0.010326, 0.032297]


# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='blue')
plt.plot(tamanos, tiempo_cpp, label='C++', color='orange')
plt.plot(tamanos, tiempo_java, label='Java', color='red')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (ms)')
plt.title('Tiempo de ejecución de Couting Sort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
