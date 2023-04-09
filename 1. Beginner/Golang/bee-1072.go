package main

import "fmt"

func main() {
	var num, in, out, x int
	fmt.Scan(&num)

	for i := 0; i < num; i++ {
		fmt.Scan(&x)
		if x <= 20 && x >= 10 {
			in++
		} else {
			out++
		}
	}
	fmt.Println(in, "in")
	fmt.Println(out, "out")
}
