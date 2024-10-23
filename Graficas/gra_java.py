import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_bubble = [0.001148, 0.001489, 0.016104, 0.020890, 0.034181, 0.055631, 0.105868, 0.119062, 0.170978, 0.242290, 0.311986, 0.578140, 2.348098, 5.870169, 8.747070, 18.743265, 28.604884, 31.622173, 41.991468, 57.165788, 68.493833]
tiempo_couting=[0.000022, 0.000149, 0.000184, 0.000199, 0.000211, 0.000252, 0.000311, 0.000322, 0.000360, 0.000928, 0.001001, 0.002236, 0.002413, 0.003236, 0.003280, 0.004505, 0.005064, 0.005086, 0.006692, 0.010326, 0.032297]
tiempo_heap=[0.000137, 0.000278, 0.000621, 0.000723, 0.000780, 0.001098, 0.001354, 0.001425, 0.001862, 0.002019, 0.002492, 0.006743, 0.009680, 0.013597, 0.016128, 0.020321, 0.027908, 0.030418, 0.041336, 0.041513, 0.053242]
tiempo_insertion=[0.000332, 0.000472, 0.006123, 0.009136, 0.013214, 0.014672, 0.022545, 0.031216, 0.044292, 0.054055, 0.073641, 0.105070, 0.465539, 0.836453, 1.668259, 3.139857, 5.921116, 6.657945, 9.409565, 13.946793, 15.220577]
tiempo_merge=[0.000130, 0.000732, 0.000920, 0.001006, 0.001326, 0.001552, 0.001865, 0.002380, 0.002967, 0.003119, 0.003360, 0.007121, 0.010703, 0.012693, 0.015796, 0.019778, 0.023341, 0.026932, 0.027300, 0.032195, 0.044084 ]
tiempo_quick=[0.000254, 0.000419, 0.001058, 0.001096, 0.001708, 0.002366, 0.002740, 0.002793, 0.002990, 0.003055, 0.004571, 0.005886, 0.011179, 0.012124, 0.013315, 0.013693, 0.015670, 0.019509, 0.023201, 0.025223, 0.043227]
tiempo_selection=[0.000329, 0.000983, 0.006472, 0.009681, 0.014126, 0.018090, 0.025461, 0.027023, 0.059589, 0.100021, 0.117056, 0.237868, 0.852601, 1.897676, 2.693849, 5.509852, 8.458457, 9.091789, 11.018678, 11.648134, 16.046561]


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
plt.title('Tiempo de ejecución de los Algoritmos de Ordenamiento en Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()