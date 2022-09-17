package main

import (
	"fmt"
)

func main() {
	var (
		n, m int
		k, v string
	)
	fmt.Scan(&n)
	for n != 0 {
		attend := make(map[string]string)
		for i := 0; i < n; i++ {
			fmt.Scan(&k, &v)
			attend[k] = v
		}
		fmt.Scan(&m)
		cnt := 0
		for i := 0; i < m; i++ {
			fmt.Scan(&k, &v)
			if attend[k] != v {
				x, y := attend[k], v
				cnt2 := 0
				for j := 0; j < len(x); j++ {
					if string(x[j]) != string(y[j]) {
						cnt2++
					}
				}
				if cnt2 > 1 {
					cnt += 1
				}
			}
		}
		fmt.Println(cnt)
		fmt.Scan(&n)
	}
}
