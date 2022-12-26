package main

import "fmt"

func main() {
	x := 0
	fmt.Scan(&x)

	for i := 1; i <= x; i++ {
		if x%i == 0 {
			fmt.Println(i)
		}
	}
}
