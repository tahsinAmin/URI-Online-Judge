package main

import "fmt"

func main() {
	var a, n int
	result := 0

	fmt.Scan(&a)
	for true {
		fmt.Scan(&n)
		if n > 0 {
			break
		}
	}
	for ; n > 0; n-- {
		result += a
		a++
	}
	fmt.Println(result)
}
