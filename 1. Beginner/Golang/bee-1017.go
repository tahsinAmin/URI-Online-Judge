package main

import (
	"fmt"
)

func main() {
	var x, y float64
	fmt.Scan(&x)
	fmt.Scan(&y)
	fmt.Printf("%.3f\n", (x*y)/2.0);

}