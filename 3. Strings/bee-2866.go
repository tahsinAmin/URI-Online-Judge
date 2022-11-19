package main

import "fmt"

func main() {
	var (
		n  int
		p1 string
		v  []string
	)
	alphaMap := map[string]string{"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h", "i": "i", "j": "j", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"}

	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&p1)
		v = append(v, p1)
	}
	for i := 0; i < len(v); i++ {
		s := ""
		for k := 0; k < len(v[i]); k++ {
			_, isPresent := alphaMap[v[i][k:k+1]]
			if isPresent {
				s = v[i][k:k+1] + s
			}
		}
		fmt.Println(s)
	}
}
