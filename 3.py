def mergesort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    mergesort(arr, left, mid)
    mergesort(arr, mid + 1, right)

    left_part = arr[left : mid + 1]
    right_part = arr[mid + 1 : right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

arr = [105, 22, 1001, 45, 12]
mergesort(arr, 0, len(arr) - 1)
print("In-place результат:", arr)
