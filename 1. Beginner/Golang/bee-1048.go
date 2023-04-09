package main

import (
	"fmt"
)

func salaryInc(s float64, i float64) {
	var nSal float64
	nSal = s + s*i
	fmt.Printf("Novo salario: %.2f\n", nSal)
	fmt.Printf("Reajuste ganho: %.2f\n", s*i)
	fmt.Println("Em percentual:", int(i*100), "%")
}

func main() {
	var s float64
	fmt.Scan(&s)
	if s >= 0 && s <= 400 {
		salaryInc(s, 0.15)
	} else if s > 400 && s <= 800 {
		salaryInc(s, 0.12)
	} else if s > 800 && s <= 1200 {
		salaryInc(s, 0.10)
	} else if s > 1200 && s <= 2000 {
		salaryInc(s, 0.07)
	} else {
		salaryInc(s, 0.04)
	}
}
