import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_bubble = [0, 0.001006, 0.005624, 0.023044, 0.054206, 0.9315, 0.141827, 0.185299, 0.268696, 0.337879, 0.428911, 0.531784, 
              2.17231, 5.84647, 12.0642, 20.2983, 28.8577, 40.7651, 54.469, 68.2499, 87.869]
tiempo_couting=[0, 0,0,0,0,0,0,0,0,0.001001,0,0,0,0.001001,0.001,0.000999,0.001,0.002307,0.000999,0.00203,0.003012]
tiempo_heap=[0, 0,0,0,0,0,0,0,0,0.001001,0,0,0,0.001001,0.001,0.000999,0.001,0.002307,0.000999,0.00203,0.003012]
tiempo_insertion=[0,0.001003,0.001999,0.006512,0.013,0.021512,0.031168,0.043168,0.06264,0.078146,0.096662,0.123498,0.479742,1.54135,2.74578,4.33248,6.22688,7.68918,10.9975,14.0827,16.9522]
tiempo_merge=[0, 0.004550, 0.007999,0.005642, 0.008016, 0.013295,0.021159, 0.029097,0.020176, 0.023819, 0.022023, 0.032118 , 0.071996, 0.117075 , 0.153642, 0.210024, 0.252781 , 0.293793,0.240449,0.277799,0.429942 ]
tiempo_quick=[0,0,0,0.000504,0,0.000999,0.001,0.001002,0,0.001005,0.000936,0.000999,0.003004,0.005915,0.007634,0.010995,0.01899,0.015063,0.022007,0.029584,0.030521 ]
tiempo_selection=[0,0.000999,0.001996,0.007513,0.018,0.028605,0.044004,0.058633,0.08339,0.106155,0.134208,0.170892,0.831157,2.15616,3.72169,5.92684,8.6674,11.0692,14.5082,19.338,22.8978]


# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_bubble, label='Bubble', color='blue')
plt.plot(tamanos, tiempo_couting, label='Couting', color='orange')
plt.plot(tamanos, tiempo_heap, label='Heap', color='red')
plt.plot(tamanos, tiempo_insertion, label='Insertion', color='black')
plt.plot(tamanos, tiempo_merge, label='Merge', color='pink')
plt.plot(tamanos, tiempo_quick, label='Quick', color='brown')
plt.plot(tamanos, tiempo_selection, label='Selection', color='green')

# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de los Algoritmos de Ordenamiento en C++')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()