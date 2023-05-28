package main

import (
	"fmt"
	"math"
)

func main() {
	var x1,y1,x2,y2 float64

	fmt.Scan(&x1)
	fmt.Scan(&y1)
	fmt.Scan(&x2)
	fmt.Scan(&y2)

	fmt.Printf("%.4f\n", math.Sqrt(math.Pow(x2 - x1, 2) + math.Pow(y2 - y1, 2)));

}