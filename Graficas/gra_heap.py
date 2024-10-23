import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0, 0, 0.008003,0.009930, 0.016004, 0.020668, 0.022941, 0.030107, 0.041261, 0.041224, 0.034882, 0.048084, 0.131092, 0.190069, 0.282604, 0.400307, 0.424450, 0.501486, 0.572166,0.478676, 0.751072]
tiempo_cpp = [0, 0,0,0,0,0,0,0,0,0.001001,0,0,0,0.001001,0.001,0.000999,0.001,0.002307,0.000999,0.00203,0.003012]
tiempo_java=[0.000137, 0.000278, 0.000621, 0.000723, 0.000780, 0.001098, 0.001354, 0.001425, 0.001862, 0.002019, 0.002492, 0.006743, 0.009680, 0.013597, 0.016128, 0.020321, 0.027908, 0.030418, 0.041336, 0.041513, 0.053242]
# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='blue')
plt.plot(tamanos, tiempo_cpp, label='C++', color='orange')
plt.plot(tamanos, tiempo_java, label='Java', color='red')


# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (ms)')
plt.title('Tiempo de ejecución de HeapSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
