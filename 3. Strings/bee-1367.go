// https://www.beecrowd.com.br/judge/en/problems/view/1367

package main

import (
	"fmt"
)

func contains(s []string, e string) bool {
	fmt.Println("We have", s, e)
	for _, a := range s {
		if a == e {
			return true
		}
	}

	return false
}

func main() {

	var n int
	fmt.Scan(&n)
	for n != 0 {
		cnt, total, distinct_c, distinct_inc := 0, 0, make([]string, n), make([]string, n)

		for j := 0; j < n; j++ {
			var a string
			var c string
			var b int
			fmt.Scan(&a, &b, &c)

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
		fmt.Scan(&n)
	}
}
