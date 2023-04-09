package main

import "fmt"

func main() {
	var num float32
	positivos := 0

	for i := 0; i < 6; i++ {
		fmt.Scan(&num)
		if num > 0 {
			positivos++
		}
	}

	fmt.Println(positivos, "valores positivos")
}
