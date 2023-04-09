package main

import "fmt"

func main() {
	var (
		num                      int
		one, two, three, average float64
	)
	fmt.Scan(&num)

	for i := 0; i < num; i++ {
		fmt.Scan(&one, &two, &three)
		average = (one*2 + two*3 + three*5) / 10
		fmt.Printf("%.1f\n", average)
	}
}
