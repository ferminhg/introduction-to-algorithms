package main

import "fmt"

func insertionSort(arrayToSort []int) []int {
	for j := 1; j < len(arrayToSort); j++ {
		key := arrayToSort[j]
		i := j - 1
		for i >= 0 && arrayToSort[i] > key {
			arrayToSort[i+1] = arrayToSort[i]
			i = i - 1
		}
		arrayToSort[i+1] = key
	}
	return arrayToSort
}

func main() {
	arrayToSort := []int{20, 10, 30, 50, 40}
	fmt.Println(insertionSort(arrayToSort))
}
