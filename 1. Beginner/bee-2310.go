package main

import "fmt"

func main() {
	var (
		n          int
		s          string
		v1, v2, v3 float64
	)
	var ar1 [3]float64
	var ar2 [3]float64

	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		fmt.Scan(&s)
		fmt.Scan(&v1, &v2, &v3)
		ar1[0] += v1
		ar1[1] += v2
		ar1[2] += v3
		fmt.Scan(&v1, &v2, &v3)
		ar2[0] += v1
		ar2[1] += v2
		ar2[2] += v3
	}

	fmt.Printf("Pontos de Saque: %.2f %%.\n", ((ar2[0] / ar1[0]) * 100))
	fmt.Printf("Pontos de Bloqueio: %.2f %%.\n", ((ar2[1] / ar1[1]) * 100))
	fmt.Printf("Pontos de Ataque: %.2f %%.\n", ((ar2[2] / ar1[2]) * 100))
}
