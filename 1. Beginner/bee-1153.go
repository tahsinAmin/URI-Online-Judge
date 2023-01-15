package main

import "fmt"

func main() {
	x := 0
	multiply := 1
	fmt.Scan(&x)

	for i := x; i > 0; i-- {
		multiply *= i
	}
	fmt.Println(multiply)
}
