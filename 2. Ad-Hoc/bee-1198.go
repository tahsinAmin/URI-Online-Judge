package main

import (
	"fmt"
	"strconv"
	"unicode"
)

func main() {
	var n int
	var s string

	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		fmt.Scan(&s)
		x, _ := strconv.Atoi(string(s[0]))
		y, _ := strconv.Atoi(string(s[2]))

		if x == y {
			fmt.Println(x * y)
		} else if unicode.IsUpper(rune(s[1])) {
			fmt.Println(y - x)
		} else {
			fmt.Println(y + x)
		}
	}
}
