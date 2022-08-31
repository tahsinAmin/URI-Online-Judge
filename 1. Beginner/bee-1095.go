package main

import "fmt"

func main() {
	var i, j = 1, 60

	for j != -5 {
		fmt.Printf("I=%v J=%v\n", i, j)
		i += 3
		j -= 5
	}
}
