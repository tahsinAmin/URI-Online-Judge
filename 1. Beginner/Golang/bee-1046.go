package main

import (
	"fmt"
)

func main() {
	var A, B, C int

	fmt.Scan(&A, &B)
	C = 0

	for i := A; i < 25; i++ {
		if A == B {
			fmt.Println("O JOGO DUROU 24 HORA(S)")
			break
		}
		if i == 24 {
			i = 0
		}
		if i == B {
			fmt.Printf("O JOGO DUROU %d HORA(S)\n", C)
			break
		}
		C++
	}
}
