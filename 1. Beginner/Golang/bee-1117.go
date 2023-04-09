package main

import "fmt"

func main () {
	grades := readInput()
	average := calculate(grades)
	printResult(average)
}

func readInput () [2]float64 {
	counter, inp := 0, 0.0
	var grades [2]float64

	for counter < 2 {
		fmt.Scan(&inp)
		if ! isValid(inp) {
			fmt.Println("nota invalida")
			continue
		}
		grades[counter] = inp
		counter++
	}
	return grades
}

func isValid(grade float64) bool {
	return grade >= 0 && grade <= 10
}

func calculate(grades [2]float64) float64 {
	return (grades[0] + grades[1]) / 2
}

func printResult(average float64) {
	fmt.Printf("media = %.2f\n", average)
}