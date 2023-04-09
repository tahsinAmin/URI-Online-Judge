package main

import "fmt"

func main() {
	var num int
	fmt.Scan(&num)

	for i := 2; i <= 10000; i += num {
		fmt.Println(i)
	}
}
