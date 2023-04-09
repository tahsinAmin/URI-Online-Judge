package main

import "fmt"

func main() {
	var x, y int
	fmt.Scan(&x, &y)
	if y%x == 0 || x%y == 0 {
		fmt.Println("Sao Multiplos")
	} else {
		fmt.Println("Nao sao Multiplos")
	}
}
