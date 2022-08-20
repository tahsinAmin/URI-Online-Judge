package main

import "fmt"

func main() {
	var num, sum, positivos float32

	for i := 0; i < 6; i++ {
		fmt.Scan(&num)
		if num > 0 {
			positivos++
			sum += num
		}
	}

	fmt.Printf("%.0f valores positivos\n", positivos)
	fmt.Printf("%.1f\n", sum/positivos)
}
