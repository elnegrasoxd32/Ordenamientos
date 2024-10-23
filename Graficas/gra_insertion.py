import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0, 0.005066, 0.023998,0.149823, 0.304275, 0.574191, 0.901168, 1.260937,1.928923, 2.218269, 2.096119, 3.343124, 15.310636, 33.504431, 61.803772, 96.149905, 142.182067,  188.938009,218.530065,236.145497,407.149290]
tiempo_java=[0.000332, 0.000472, 0.006123, 0.009136, 0.013214, 0.014672, 0.022545, 0.031216, 0.044292, 0.054055, 0.073641, 0.105070, 0.465539, 0.836453, 1.668259, 3.139857, 5.921116, 6.657945, 9.409565, 13.946793, 15.220577]
tiempo_cpp=[0,0.001003,0.001999,0.006512,0.013,0.021512,0.031168,0.043168,0.06264,0.078146,0.096662,0.123498,0.479742,1.54135,2.74578,4.33248,6.22688,7.68918,10.9975,14.0827,16.9522]

# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='blue')
plt.plot(tamanos, tiempo_cpp, label='C++', color='orange')
plt.plot(tamanos, tiempo_java, label='Java', color='red')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de InsertionSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()