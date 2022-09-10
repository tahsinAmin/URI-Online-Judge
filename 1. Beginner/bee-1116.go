package main

import "fmt"

func main() {
	var n int
	var f, x, y float32
	fmt.Scan(&n)
	for n > 0 {
		fmt.Scan(&x, &y)
		if y == 0 {
			fmt.Println("divisao impossivel")
		} else {
			f = x / y
			fmt.Printf("%.1f\n", f)
		}
		n--
	}
}
