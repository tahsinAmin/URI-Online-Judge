package main

import "fmt"

func main() {
	var n, x, y, temp, sum int
	fmt.Scan(&n)
	a := make([]int, n)

	for s := 0; s < n; s++ {
		fmt.Scan(&x, &y)
		if x <= y {
		} else {
			temp = x
			x = y
			y = temp
		}
		sum = 0
		for i := x + 1; i < y; i++ {
			if i%2 == 1 {
				sum += i
			}
		}
		a[s] = sum
	}
	for x := 0; x < n; x++ {
		fmt.Println(a[x])
	}
}
	