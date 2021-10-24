def insertionSort(arrayToSort):
    for j in range(1, len(arrayToSort)-1):
        key = arrayToSort[j]
        i = j-1
        while i >= 0 and arrayToSort[i] > key:
            arrayToSort[i+1] = arrayToSort[i]
            i = i - 1
        arrayToSort[i+1] = key
    return arrayToSort

assert insertionSort([3,4,5,1,2,6]) == [1,2,3,4,5,6]
