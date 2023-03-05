package main

import "fmt"

func main() {
	m := 0

	fmt.Scan(&m)

	for i := 1; i <= m*4; i++ {
		if i % 4 != 0 {
			fmt.Print(i, " ")
		}else {
			fmt.Println("PUM")
		}

	}
}
