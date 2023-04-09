package main

import "fmt"

func main () {
	
	var x, y, sum int

	fmt.Scan(&x)
	fmt.Scan(&y)
	
	if x > y {
		x, y = y, x
	}

	for i := x; i <= y; i++ {
		if i % 13 == 0 {
			continue
		}
		sum += i
		
	}
	fmt.Println(sum)
}

