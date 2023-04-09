package main

import "fmt"

func main() {
	var x int
	for {
		fmt.Scan(&x)
		if x == 2002 {
			fmt.Println("Acesso Permitido")
			break
		}
		fmt.Println("Senha Invalida")
	}
}
