import os
import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Counting Sort
def counting_sort(arr):
    if len(arr) == 0:
        return arr
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1
    
    count = [0] * range_of_elements
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_value] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_value] - 1] = arr[i]
        count[arr[i] - min_value] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

# Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    return numbers

def main():
    folder_path = r"C:\Users\TOTI\Desktop\aleatorios_txt"  # Usar cadena cruda
    bubble_sort_times = []
    counting_sort_times = []
    heap_sort_times = []
    insertion_sort_times = []
    merge_sort_times = []
    quick_sort_times = []
    selection_sort_times = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            numbers = read_numbers_from_file(file_path)
            
            # Bubble Sort
            numbers_copy = numbers[:]  # Copia para no modificar el original
            start_time = time.time()
            bubble_sort(numbers_copy)
            end_time = time.time()
            bubble_sort_times.append((end_time - start_time, filename))
            
            # Counting Sort
            numbers_copy = numbers[:]  # Otra copia
            start_time = time.time()
            counting_sort(numbers_copy)
            end_time = time.time()
            counting_sort_times.append((end_time - start_time, filename))

            # Heap Sort
            numbers_copy = numbers[:]  # Otra copia
            start_time = time.time()
            heap_sort(numbers_copy)
            end_time = time.time()
            heap_sort_times.append((end_time - start_time, filename))

            # Insertion Sort
            numbers_copy = numbers[:]  # Otra copia
            start_time = time.time()
            insertion_sort(numbers_copy)
            end_time = time.time()
            insertion_sort_times.append((end_time - start_time, filename))

            # Merge Sort
            numbers_copy = numbers[:]  # Otra copia
            start_time = time.time()
            merge_sort(numbers_copy)
            end_time = time.time()
            merge_sort_times.append((end_time - start_time, filename))

            # Quick Sort
            numbers_copy = numbers[:]  # Otra copia
            start_time = time.time()
            numbers_copy = quick_sort(numbers_copy)  # Quick Sort retorna una nueva lista
            end_time = time.time()
            quick_sort_times.append((end_time - start_time, filename))

            # Selection Sort
            numbers_copy = numbers[:]  # Otra copia
            start_time = time.time()
            selection_sort(numbers_copy)
            end_time = time.time()
            selection_sort_times.append((end_time - start_time, filename))

    # Ordenar los tiempos por nombre de archivo
    bubble_sort_times.sort(key=lambda x: x[1])
    counting_sort_times.sort(key=lambda x: x[1])
    heap_sort_times.sort(key=lambda x: x[1])
    insertion_sort_times.sort(key=lambda x: x[1])
    merge_sort_times.sort(key=lambda x: x[1])
    quick_sort_times.sort(key=lambda x: x[1])
    selection_sort_times.sort(key=lambda x: x[1])

    # Imprimir los tiempos de cada algoritmo
    print("Tiempos de Bubble Sort:")
    for elapsed_time, filename in bubble_sort_times:
        print(f'Tiempo de ordenamiento para {filename} (Bubble Sort): {elapsed_time:.6f} segundos')

    print("\nTiempos de Counting Sort:")
    for elapsed_time, filename in counting_sort_times:
        print(f'Tiempo de ordenamiento para {filename} (Counting Sort): {elapsed_time:.6f} segundos')

    print("\nTiempos de Heap Sort:")
    for elapsed_time, filename in heap_sort_times:
        print(f'Tiempo de ordenamiento para {filename} (Heap Sort): {elapsed_time:.6f} segundos')

    print("\nTiempos de Insertion Sort:")
    for elapsed_time, filename in insertion_sort_times:
        print(f'Tiempo de ordenamiento para {filename} (Insertion Sort): {elapsed_time:.6f} segundos')

    print("\nTiempos de Merge Sort:")
    for elapsed_time, filename in merge_sort_times:
        print(f'Tiempo de ordenamiento para {filename} (Merge Sort): {elapsed_time:.6f} segundos')

    print("\nTiempos de Quick Sort:")
    for elapsed_time, filename in quick_sort_times:
        print(f'Tiempo de ordenamiento para {filename} (Quick Sort): {elapsed_time:.6f} segundos')

    print("\nTiempos de Selection Sort:")
    for elapsed_time, filename in selection_sort_times:
        print(f'Tiempo de ordenamiento para {filename} (Selection Sort): {elapsed_time:.6f} segundos')

if __name__ == '__main__':
    main()