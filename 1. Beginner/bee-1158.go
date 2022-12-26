package main

import "fmt"

func main() {
	var x, y, z, sum int
	fmt.Scan(&x)
	for i := 0; i < x; i++ {
		sum = 0
		fmt.Scan(&y, &z)
		j := 0
		if y%2 == 0 {
			y += 1
		} else {
			sum = y
			j += 1
			y += 2
		}
		for ; j < z; j++ {
			sum += y
			y += 2
		}
		fmt.Println(sum)
	}
}
