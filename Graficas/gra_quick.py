import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0, 0, 0,0.008209, 0.008058 , 0.006518,0.004543, 0.011907,0.016306,0.016234,0.010522, 0.016504, 0.024118 , 0.038180, 0.052007 , 0.069793, 0.086989, 0.089691 , 0.085635,0.105802,0.150354 ]
tiempo_java=[0.000254, 0.000419, 0.001058, 0.001096, 0.001708, 0.002366, 0.002740, 0.002793, 0.002990, 0.003055, 0.004571, 0.005886, 0.011179, 0.012124, 0.013315, 0.013693, 0.015670, 0.019509, 0.023201, 0.025223, 0.043227]
tiempo_cpp=[0,0,0,0.000504,0,0.000999,0.001,0.001002,0,0.001005,0.000936,0.000999,0.003004,0.005915,0.007634,0.010995,0.01899,0.015063,0.022007,0.029584,0.030521]

# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='blue')
plt.plot(tamanos, tiempo_cpp, label='C++', color='orange')
plt.plot(tamanos, tiempo_java, label='Java', color='red')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (ms)')
plt.title('Tiempo de ejecución de QuickSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()