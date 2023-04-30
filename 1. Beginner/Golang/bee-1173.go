package main

import "fmt"

func main() {
	var n int

	fmt.Scan(&n)
	var a [10]int

	a[0] = n
	fmt.Printf("N[%d] = %d\n", 0, n)

	for i := 1; i < 10; i++ {
		a[i]  = a[i-1] * 2
		fmt.Printf("N[%d] = %d\n", i, a[i])
	}
}
