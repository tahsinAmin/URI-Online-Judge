package main

import (
	"fmt"
	"sort"
)

func main() {
	var A, B, C float64

	fmt.Scan(&A, &B, &C)

	lados := []float64{A, B, C}

	sort.Slice(lados, func(i, j int) bool { // Descending order slice
		return lados[i] > lados[j]
	})

	A, B, C = lados[0], lados[1], lados[2]

	for i := 0; i < 1; i++ {
		if A >= (B + C) {
			fmt.Println("NAO FORMA TRIANGULO")
			break
		}
		if A*A == (B*B + C*C) {
			fmt.Println("TRIANGULO RETANGULO")
		} else if A*A > (B*B + C*C) {
			fmt.Println("TRIANGULO OBTUSANGULO")
		} else {
			fmt.Println("TRIANGULO ACUTANGULO")
		}
		if A == B && B == C {
			fmt.Println("TRIANGULO EQUILATERO")
			break
		}
		if (B == A) || (A == C) || (C == B) {
			fmt.Println("TRIANGULO ISOSCELES")
		}
	}
}
