package main

import "fmt"

func main() {
	var x int

	for i := 1; i > 0; i++ {
		fmt.Scan(&x)
		if x == 0 {
			break
		}
		j := 1
		for ; j < x; j++ {
			fmt.Print(j, " ")
		}
		fmt.Print(j)
		fmt.Println("")
	}
}
