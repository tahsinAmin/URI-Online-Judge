package main

import "fmt"

func main() {
	var s float64
	fmt.Scan(&s)

	if s > 2000 {
		if s > 3000 {
			if s > 4500 {
				fmt.Printf("R$ %.2f\n", ((1000 * 0.08) + (1500 * 0.18) + ((s - 4500) * 0.28)))
			} else {
				fmt.Printf("R$ %.2f\n", ((1000 * 0.08) + ((s - 3000) * 0.18)))
			}
		} else {
			fmt.Printf("R$ %.2f\n", ((s - 2000) * 0.08))
		}
	} else {
		fmt.Println("Isento")
	}
}
