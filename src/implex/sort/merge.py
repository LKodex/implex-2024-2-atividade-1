from math import floor

def sort(arr: list = list()) -> list:
    sortedArr = arr.copy()
    __merge_sort(sortedArr, 0, len(sortedArr) - 1)
    return sortedArr

def __merge_sort(arr: list, p, r):
    if p < r:
        q = floor((p + r) / 2)
        __merge_sort(arr, p, q)
        __merge_sort(arr, q + 1, r)
        __merge(arr, p, q, r)
    return arr

def __merge(arr: list, p, q, r) -> list:
    i = 0
    j = 0
    for k in range(p, r + 1):
        if arr[p + i] <= arr[q + j]:
            arr[k] = arr[p + i]
            i += 1
        else:
            arr[k] = arr[q + j]
            j += 1
    return arr
