import random
def generar_numeros_aleatorios(nombre_archivo, N, rango_min, rango_max):
    with open(nombre_archivo, 'w') as archivo:
        for _ in range(N):
            numero = random.randint(rango_min, rango_max)
            archivo.write(f"{numero}\n")

nombre_archivo = "9000.txt"
N = int(input("Ingresa la cantidad de números aleatorios: "))
rango_min = int(input("Ingresa el límite inferior del rango: "))
rango_max = int(input("Ingresa el límite superior del rango: "))
generar_numeros_aleatorios(nombre_archivo, N, rango_min, rango_max)
print(f"Archivo {nombre_archivo} generado con {N} números aleatorios.")
