package main

import "fmt"

func main() {
	var num, positivos int

	for i := 0; i < 5; i++ {
		fmt.Scan(&num)
		if num%2 == 0 {
			positivos++
		}
	}

	fmt.Println(positivos, "valores pares")
}
