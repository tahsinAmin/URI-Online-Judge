package main

import (
	"fmt"
)

func main() {
	var x, y int
	price := [6]float64{0.0, 4.00, 4.50, 5.00, 2.00, 1.50}

	fmt.Scanf("%v %v", &x, &y)
	fmt.Printf("Total: R$ %0.2f\n", price[x] * float64(y))
}