package main

import "fmt"

func main() {
	var x, y int
	fmt.Scan(&x, &y)

	for true {
		if x == 0 || y == 0 {
			break
		}
		if x > 0 && y > 0 {
			fmt.Println("primeiro")
		} else if x > 0 && y < 0 {
			fmt.Println("quarto")
		} else if x < 0 && y > 0 {
			fmt.Println("segundo")
		} else {
			fmt.Println("terceiro")
		}
		fmt.Scan(&x, &y)
	}
}
