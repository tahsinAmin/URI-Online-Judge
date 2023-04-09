package main

import "fmt"

func main() {
	var i, j, rep = 1, 7, 0
	for i < 10 {
		rep = 1
		for rep != 4 {
			fmt.Printf("I=%v J=%v\n", i, j)
			j--
			rep++
		}
		j += 5
		i += 2
	}
}
