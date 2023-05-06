package main

import "fmt"

func main() {
	var h1, m1, h2, m2 int
	for {
		fmt.Scan(&h1, &m1, &h2, &m2)
		if h1 == 0 && h2 == 0 && m1 == 0 && m2 == 0 {
			break
		}
		min := 0
		if h1 == h2 {
			if m1 == m2 {
				min = 1440
			}
			if m1 > m2 {
				min = 1440 + (m2 - m1)
			} else {
				min += m2 - m1
			}
		} else if h1 < h2 {
			min = (h2-h1)*60 + (m2 - m1)
		} else {
			min = (24-h1)*60 + (h2 * 60) + (m2 - m1)
		}
		fmt.Println(min)
	}
}
