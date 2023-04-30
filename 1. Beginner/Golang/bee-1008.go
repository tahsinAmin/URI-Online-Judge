package main

import "fmt"

func main() {
	var a int
	var b, c float64

	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&c)

	fmt.Println("NUMBER =", a);

	fmt.Printf("SALARY = U$ %.2f\n", (b*c))
}