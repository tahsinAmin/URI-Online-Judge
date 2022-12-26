package main

import "fmt"

func main() {
	x := 0
	fmt.Scan(&x)
	for x != 0 {
		sum := 0
		if x%2 == 0 {
			sum += 5*x + 20
		} else {
			x += 1
			sum += 5*x + 20
		}
		fmt.Println(sum)
		fmt.Scan(&x)
	}
}
