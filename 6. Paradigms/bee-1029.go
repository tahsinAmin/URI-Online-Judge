package main

import "fmt"

var cnt int

func main() {
	var n, x, calls int
	fmt.Scan(&n)

	for n > 0 {
		fmt.Scan(&x)
		cnt = 0
		calls = fib(x)
		fmt.Printf("fib(%d) = %d calls = %d\n", x, cnt-1, calls)
		n--
	}
}

func fib(num int) int {
	cnt++
	if num == 1 {
		return 1
	}
	if num == 0 {
		return 0
	}
	return fib(num-1) + fib(num-2)
}
