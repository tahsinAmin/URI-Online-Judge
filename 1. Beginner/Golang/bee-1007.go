package main

import "fmt"

func main() {
	var a, b, c, d int

	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&c)
	fmt.Scan(&d)

	fmt.Println("DIFERENCA =", (a*b)-(c*d));
}