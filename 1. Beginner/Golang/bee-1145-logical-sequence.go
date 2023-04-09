package main

import "fmt"

func main() {
	var m, n, cnt int
	fmt.Scan(&m, &n)
	cnt = 1
	for i := 1; i <= n; i++ {
		if cnt == m {
			fmt.Println(i)
			cnt = 1
		} else {
			fmt.Print(i, " ")
			cnt += 1
		}
	}
}
