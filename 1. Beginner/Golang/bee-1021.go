package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	notes := [12]float64{100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01}
	val := [12]int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

	var remains float64
	fmt.Scan(&remains)

	fmt.Println("NOTAS:")
	for i := 0; i < 6; i++ {
		if remains >= notes[i] {
			val[i] = int(remains / notes[i])
			remains, _ = strconv.ParseFloat(fmt.Sprintf("%.2f", math.Mod(remains, notes[i])), 64)
		}
		fmt.Printf("%d nota(s) de R$ %.2f\n", val[i], notes[i])
	}
	fmt.Println("MOEDAS:")
	for i := 6; i < 12; i++ {
		if remains >= notes[i] {
			val[i] = int(remains / notes[i])
			remains, _ = strconv.ParseFloat(fmt.Sprintf("%.2f", math.Mod(remains, notes[i])), 64)
		}
		fmt.Printf("%d moeda(s) de R$ %.2f\n", val[i], notes[i])
	}
}
