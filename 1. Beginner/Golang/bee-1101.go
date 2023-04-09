package main

import "fmt"

func main() {
	var x, y, sum int

	for {
		fmt.Scan(&x, &y)
		if x <= 0 || y <= 0 {
			break
		}
		if x > y {
			x, y = y, x
		}
		fmt.Print(x)
		sum = x
		for i := x + 1; i <= y; i++ {
			fmt.Print(" ", i)
			sum += i
		}
		fmt.Printf(" Sum=%d\n", sum)
	}
}
