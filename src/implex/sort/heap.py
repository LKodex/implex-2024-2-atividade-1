def sort(arr: list = list()) -> list:
    sortedArr = arr.copy()
    n = len(sortedArr)

    for i in range(n // 2 - 1, -1, -1):
        __heapify(sortedArr, n, i)

    for i in range(n - 1, 0, -1):
        sortedArr[i], sortedArr[0] = sortedArr[0], sortedArr[i]
        __heapify(sortedArr, i, 0)

    return sortedArr

def __heapify(arr: list, n: int, i: int):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        __heapify(arr, n, largest)  
