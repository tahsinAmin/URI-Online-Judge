package main

import "fmt"

func main() {
	var x int
	fmt.Scan(&x)
	for i := 2; i <= x; i += 2 {
		fmt.Printf("%v^%v = %v\n", i, 2, (i * i))
	}
}
