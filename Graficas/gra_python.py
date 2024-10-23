import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_bubble = [0, 0.15404, 0.644252, 0.295745, 0.657684, 1.235036, 1.966616, 2.768904, 4.090429, 5.018629, 4.514349, 7.481925,
                 31.271869, 71.937347, 126.341653, 198.761662, 283.951078, 389.077420, 513.654444, 473.212725, 788.981539]
tiempo_couting=[0, 0.003531, 0.000000,0, 0, 0, 0.002051, 0.000000, 0.004521, 0, 0.003520, 0.008029, 0.003012, 0.020983, 0.019658, 0.019328, 0.031728, 0.024971, 0.032568, 0.029566, 0.050189]
tiempo_heap=[0, 0, 0.008003,0.009930, 0.016004, 0.020668, 0.022941, 0.030107, 0.041261, 0.041224, 0.034882, 0.048084, 0.131092, 0.190069, 0.282604, 0.400307, 0.424450, 0.501486, 0.572166,0.478676, 0.751072]
tiempo_insertion=[0, 0.005066, 0.023998,0.149823, 0.304275, 0.574191, 0.901168, 1.260937,1.928923, 2.218269, 2.096119, 3.343124, 15.310636, 33.504431, 61.803772, 96.149905, 142.182067,  188.938009,218.530065,236.145497,407.149290]
tiempo_merge=[0, 0.004550, 0.007999,0.005642, 0.008016, 0.013295,0.021159, 0.029097,0.020176, 0.023819, 0.022023, 0.032118 , 0.071996, 0.117075 , 0.153642, 0.210024, 0.252781 , 0.293793,0.240449,0.277799,0.429942 ]
tiempo_quick=[0, 0, 0,0.008209, 0.008058 , 0.006518,0.004543, 0.011907,0.016306,0.016234,0.010522, 0.016504, 0.024118 , 0.038180, 0.052007 , 0.069793, 0.086989, 0.089691 , 0.085635,0.105802,0.150354 ]
tiempo_selection=[0,0.003539,0.024062,0.121142,0.272116,0.470321,0.724041,1.041322,1.379631,1.748983,1.600389,2.621735,11.220798,26.899066,48.149431,74.350325,113.037370,148.798776,136.365295,174.405588,302.655929]


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
plt.title('Tiempo de ejecución de los Algoritmos de Ordenamiento en Python')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()