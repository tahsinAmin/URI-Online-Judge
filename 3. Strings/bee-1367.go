package main

import (
	"fmt"
)

func contains(s []string, e string) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func main() {
	var n int
	fmt.Scanln(&n)
	for n != 0 {
		var (
			cnt,
			total int
			distinct_c,
			distinct_inc []string
		)

		for j := 0; j < n; j++ {
			var (
				a,
				c string
				b int
			)
			fmt.Scanf("%s %v %s", &a, &b, &c)

			if c == "correct" && !contains(distinct_c, a) {
				cnt += 1
				distinct_c = append(distinct_c, a)
				total += b
			} else if c == "incorrect" {
				distinct_inc = append(distinct_inc, a)
			}
		}
		for _, item := range distinct_inc {
			if contains(distinct_c, item) {
				total += 20
			}
		}
		fmt.Println(cnt, total)
		fmt.Scanln(&n)
	}
}
