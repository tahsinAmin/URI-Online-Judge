package main

import (
	"fmt"
)

func main() {
	m := map[string]int{"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6}
	var n int
	var s string
	fmt.Scanln(&n)

	for i := 0; i < n; i++ {
		fmt.Scanln(&s)
		total := 0
		len_str := len(s)
		for j := 0; j < len_str; j++ {
			total += m[s[j:j+1]]
		}
		fmt.Println(total, "leds")
	}
}
