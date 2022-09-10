package main

import (
	"fmt"
)

func main() {
	var (
		test,
		multiple int
		arr []int
	)
	arr = make([]int, 5)
	// letters := [5]string{"A", "B", "C", "D", "E"}
	fmt.Scan(&test)
	for test != 0 {
		for test > 0 {
			fmt.Scan(&arr[0], &arr[1], &arr[2], &arr[3], &arr[4])
			multiple = 0
			for i := 0; i < 5; i++ {
				if arr[i] <= 127 {
					multiple++
					if multiple > 1 {
						break
					}
					// fmt.Println(letters[i])
					if i == 0 {
						fmt.Println("A")
					} else if i == 1 {
						fmt.Println("B")
					} else if i == 2 {
						fmt.Println("C")
					} else if i == 3 {
						fmt.Println("D")
					} else {
						fmt.Println("E")
					}
				}
			}
			if multiple != 1 {
				fmt.Println("*")
			}
			test--
		}
		fmt.Scan(&test)
	}
}
