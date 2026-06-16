import random

def partition_lomuto(arr, low, high):
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    
    pivot = arr[high]
    i = low   
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[high] = arr[high], arr[i]
    return i
def quicksort_random(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1 
    if low < high:
        pi = partition_lomuto(arr, low, high)
        quicksort_random(arr, low, pi - 1)
        quicksort_random(arr, pi + 1, high)  
    return arr
test = [
    [1, 2, 3, 4, 5, 6, 7],
    [7, 6, 5, 4, 3, 2, 1],
    [4, 1, 7, 3, 6, 2, 5],
    [3, 3, 3, 3, 3]
]
for arr in test:
    original = arr.copy()
    sorted_arr = quicksort_random(arr)
    print(f"Исходный: {original}")
    print(f"Отсортированный: {sorted_arr}")
    print()

# 1. Зачем нужен случайный pivot?

# Случайный pivot нужен для уменьшения вероятности систематического попадания в худший случай. Он делает алгоритм менее чувствительным к структуре входных данных.

# 2. Убирает ли он худший случай полностью?

# Нет, не убирает полностью. Теоретически случайный выбор всё ещё может привести к худшему случаю O(n²), но вероятность этого крайне мала.

# 3. Почему на практике он помогает?

# На практике случайный pivot помогает, потому что:

# Маловероятно, что все разбиения будут неудачными

# Алгоритм не зависит от злонамеренно подобранных данных

# На случайных данных вероятность плохих разбиений ничтожно мала