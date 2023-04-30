package main

import "fmt"

func main() {
	var a [10]int

	for i := 0; i < 10; i++ {
		fmt.Scan(&a[i])
		if a[i] <= 0 {
			a[i] = 1
		}
		fmt.Printf("X[%d] = %d\n", i, a[i])
	}
}
