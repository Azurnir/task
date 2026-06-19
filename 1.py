def mergesort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = mergesort(arr[:mid])
    right, inv_right = mergesort(arr[mid:])

    result = []
    i = j = 0
    inv_merge = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            for x in left[i:]:
                print(f"Инверсия: ({x}, {right[j]})")
            result.append(right[j])
            inv_merge += len(left) - i
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv_left + inv_right + inv_merge

arr = [6, 1, 2, 7, 3, 5, 8 ,9]
s_arr, count = mergesort(arr)
print(f"Отсортирован: {s_arr}, Всего инверсий: {count}")