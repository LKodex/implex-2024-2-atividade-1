def sort(arr: list = list()) -> list:
    sortedArr = arr.copy()
    for i in range(1, len(sortedArr)):
        key = sortedArr[i]
        j = i - 1
        while j >= 0 and sortedArr[j] > key:
            sortedArr[j + 1] = sortedArr[j]
            j -= 1
        sortedArr[j + 1] = key
    return sortedArr
