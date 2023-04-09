package main

import "fmt"

func main() {
	var (
		num, max, position int
	)

	for i := 1; i <= 100; i++ {
		fmt.Scan(&num)
		if num > max {
			max = num
			position = i
		}
	}
	fmt.Printf("%v\n%v\n", max, position)
}
