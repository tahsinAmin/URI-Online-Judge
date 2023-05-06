package main

import "fmt"

func main () {
	a:= [7]int{1, 3, 5, 10, 25, 50, 100}
	var t int
	fmt.Scan(&t)

	for j := 0; j < 7; j++ {
		if t <= a[j] {
			fmt.Println("Top", a[j])
			break
		}
	}
    
}