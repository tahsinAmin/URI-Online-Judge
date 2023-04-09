package main

import "fmt"

func main() {
	var x, y, total int
	fmt.Scan(&x, &y)

	if y%2 == 0 {
		y++
	} else {
		y += 2
	}

	for i := y; i < x; i += 2 {
		total += i
	}
	fmt.Println(total)
}
