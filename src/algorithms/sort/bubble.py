def sort(arr: list = list()) -> list:
    sortedArr = arr.copy()
    for i in range(len(sortedArr) - 1):
        for j in range(len(sortedArr) - 1):
            first = sortedArr[j]
            second = sortedArr[j + 1]
            
            if second < first:
                # swap
                sortedArr[j] = second
                sortedArr[j + 1] = first
    return sortedArr
