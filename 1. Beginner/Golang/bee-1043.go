package main

import "fmt"

func main() {
	var A, B, C float64
	fmt.Scanf("%v %v %v", &A, &B, &C)

	if (A+B) > C && (B+C) > A && (C+A) > B {
		fmt.Printf("Perimetro = %.1f\n", (A + B + C))
	} else {
		fmt.Printf("Area = %.1f\n", (0.5 * (A + B) * C))
	}
}
