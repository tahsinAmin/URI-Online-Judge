package main

import "fmt"

func main() {
	m := 0

	fmt.Scan(&m)

	for i := 1; i <= m; i++ {
		firstTerm := i * i
		secondTerm := firstTerm * i
		fmt.Println(i, firstTerm, secondTerm)
		fmt.Println(i, firstTerm+1, secondTerm+1)
	}
}
