import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0,0.003539,0.024062,0.121142,0.272116,0.470321,0.724041,1.041322,1.379631,1.748983,1.600389,2.621735,11.220798,26.899066,48.149431,74.350325,113.037370,148.798776,136.365295,174.405588,302.655929]
tiempo_java=[0.000329, 0.000983, 0.006472, 0.009681, 0.014126, 0.018090, 0.025461, 0.027023, 0.059589, 0.100021, 0.117056, 0.237868, 0.852601, 1.897676, 2.693849, 5.509852, 8.458457, 9.091789, 11.018678, 11.648134, 16.046561]
tiempo_cpp=[0,0.000999,0.001996,0.007513,0.018,0.028605,0.044004,0.058633,0.08339,0.106155,0.134208,0.170892,0.831157,2.15616,3.72169,5.92684,8.6674,11.0692,14.5082,19.338,22.8978]

# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='blue')
plt.plot(tamanos, tiempo_cpp, label='C++', color='orange')
plt.plot(tamanos, tiempo_java, label='Java', color='red')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de SelectionSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()