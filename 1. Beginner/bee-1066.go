package main

import "fmt"

func main() {
	var num, pares, impares, positivos, negativos int

	for i := 0; i < 5; i++ {
		fmt.Scan(&num)
		if num > 0 {
			positivos++
		} else if num < 0 {
			negativos++
		}

		if num%2 == 0 {
			pares++
		} else {
			impares++
		}
	}
	fmt.Println(pares, "valor(es) par(es)")
	fmt.Println(impares, "valor(es) impar(es)")
	fmt.Println(positivos, "valor(es) positivo(s)")
	fmt.Println(negativos, "valor(es) negativo(s)")
}
