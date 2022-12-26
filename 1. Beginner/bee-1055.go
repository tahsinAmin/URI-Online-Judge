package main

import "fmt"

func main() {
	s := 0.0
	for i := 1.0; i <= 100.0; i++ {
		s += 1 / i
	}
	fmt.Printf("%.2f\n", s)
}
