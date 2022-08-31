package main

import "fmt"

func main() {
	var i, j, rep = 1, 0, 0
	for i < 10 {
		j, rep = 7, 1
		for rep != 4 {
			fmt.Printf("I=%v J=%v\n", i, j)
			j--
			rep++
		}
		i += 2
	}
}
