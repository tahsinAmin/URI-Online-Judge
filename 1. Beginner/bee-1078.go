package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	for i := 1; i < 11; i++ {
		fmt.Println(i, "x", n, "=", n*i)
	}
}
