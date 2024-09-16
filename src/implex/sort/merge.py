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

def __merge(arr: list, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = arr[p:q+1]
    R = arr[q+1:r+1]

    i = 0  
    j = 0  
    k = p  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
