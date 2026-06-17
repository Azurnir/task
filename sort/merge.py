def _merge(left, right, compare):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]) <= 0:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort(arr, compare):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = sort(arr[:mid], compare)
    right = sort(arr[mid:], compare)
    
    result = _merge(left, right, compare)
    for i in range(len(result)):
        arr[i] = result[i]
    
    return arr