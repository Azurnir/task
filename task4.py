def partition_with_stability(arr, low, high):
    pivot = arr[high][0]
    i = low
    
    for j in range(low, high):
        if arr[j][0] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[high] = arr[high], arr[i]
    return i
def quicksort_unstable(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition_with_stability(arr, low, high)
        quicksort_unstable(arr, low, pi - 1)
        quicksort_unstable(arr, pi + 1, high)
    
    return arr
def check_stability(arr, key_index=0):
    indexed_arr = [(item[0], item[1], idx) for idx, item in enumerate(arr)]
    sorted_arr = quicksort_unstable(indexed_arr)
    stable = True
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i][0] == sorted_arr[i+1][0]:
            if sorted_arr[i][2] > sorted_arr[i+1][2]:
                stable = False
                break  
    return stable, sorted_arr
test_data = [(5, "A"), (3, "B"), (5, "C"), (2, "D"), (5, "E")]
stable, result = check_stability(test_data)

print("Исходные данные:", test_data)
print("Результат сортировки:", [(x[0], x[1]) for x in result])
print("Устойчива ли сортировка?", stable)

if not stable:
    print("\nПорядок элементов с ключом 5 нарушен")
    fives = [(x[1], x[2]) for x in result if x[0] == 5]
    print("Порядок объектов с ключом 5:", fives)
    print("Ожидалось: A, C, E (в порядке возрастания исходных индексов)")