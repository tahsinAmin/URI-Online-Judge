package main

import "fmt"

func main() {
	var num, x int
	fmt.Scan(&num)

	for i := 0; i < num; i++ {
		fmt.Scan(&x)
		if x == 0 {
			fmt.Println("NULL")
		} else {
			if x%2 == 0 {
				fmt.Print("EVEN ")
			} else {
				fmt.Print("ODD ")
			}
			if x > 0 {
				fmt.Println("POSITIVE")
			} else {
				fmt.Println("NEGATIVE")
			}
		}
	}
}
