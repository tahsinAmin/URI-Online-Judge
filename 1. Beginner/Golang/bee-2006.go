package main

import "fmt"

func main () {
	var t, x, cnt int
	fmt.Scan(&t)
	for j := 0; j < 5; j++ {
		fmt.Scan(&x)
		if t == x {
			cnt ++
		}
	}
    fmt.Println(cnt)
}