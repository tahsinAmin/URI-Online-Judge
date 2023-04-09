package main

import "fmt"

func main() {
	var n, x, flag int

	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&x)

		if x <= 1 {
			fmt.Printf("%d nao eh primo\n", x)
		}
		half_val := x / 2
		for j := 2; j <= half_val; j++ {
			if x%j == 0 {
				fmt.Printf("%d nao eh primo\n", x)
				flag = 1
				break
			}
		}

		if flag != 1 {
			fmt.Printf("%d eh primo\n", x)
		} else {
			flag = 0
		}

	}
}
