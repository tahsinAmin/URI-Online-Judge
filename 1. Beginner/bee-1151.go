package main

import "fmt"

func main() {
	var count, sum, x, z int
	fmt.Scan(&x)

	for true {
		fmt.Scan(&z)
		if z > x {
			break
		}
	}

	for i := x; sum < z; i++ {
		sum += i
		count++
	}
	fmt.Println(count)
}
