import random

def sort(arr: list = list()) -> list:
    sortedArr = arr.copy()
    __quick_sort(sortedArr, 0, len(sortedArr) - 1)
    return sortedArr

def __quick_sort(arr: list, low: int, high: int):
    if low < high:
        pi = __partition(arr, low, high)
        __quick_sort(arr, low, pi - 1)
        __quick_sort(arr, pi + 1, high)

def __partition(arr: list, low: int, high: int) -> int:
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
