const assert = require('assert');

const insertionSort = (arrayToSort) => {
    for (let j = 1; j < arrayToSort.length; j++) {
        const key =  arrayToSort[j]
        let i = j-1
        while ( i>= 0 && arrayToSort[i] > key) {
            arrayToSort[i+1] =arrayToSort[i]
            i--
        }
        arrayToSort[i+1] = key
    }
    return arrayToSort
}

assert.deepEqual(insertionSort([3,4,5,1,2,6]),[1,2,3,4,5,6])
