import matplotlib.pyplot as plt
import numpy as np

tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
tiempo_python = [0, 0.15404, 0.644252, 0.295745, 0.657684, 1.235036, 1.966616, 2.768904, 4.090429, 5.018629, 4.514349, 7.481925,
                 31.271869, 71.937347, 126.341653, 198.761662, 283.951078, 389.077420, 513.654444, 473.212725, 788.981539]
tiempo_cpp = [0, 0.001006, 0.005624, 0.023044, 0.054206, 0.9315, 0.141827, 0.185299, 0.268696, 0.337879, 0.428911, 0.531784, 
              2.17231, 5.84647, 12.0642, 20.2983, 28.8577, 40.7651, 54.469, 68.2499, 87.869]
tiempo_java=[0.001148, 0.001489, 0.016104, 0.020890, 0.034181, 0.055631, 0.105868, 0.119062, 0.170978, 0.242290, 0.311986, 0.578140, 2.348098, 5.870169, 8.747070, 18.743265, 28.604884, 31.622173, 41.991468, 57.165788, 68.493833]

plt.plot(tamanos, tiempo_python, label='Python', color='blue')
plt.plot(tamanos, tiempo_cpp, label='C++', color='orange')
plt.plot(tamanos, tiempo_java, label='Java', color='red')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de BubbleSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
