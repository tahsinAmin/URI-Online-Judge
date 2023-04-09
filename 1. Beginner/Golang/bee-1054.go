package main

import "fmt"

func main() {
	var s, counter, sum float64
	fmt.Scan(&s)

	for s >= 0 {
		sum += s
		counter++
		fmt.Scan(&s)
	}

	fmt.Printf("%.2f\n", sum/counter)
}
