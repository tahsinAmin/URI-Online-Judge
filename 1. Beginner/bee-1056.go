package main

import "fmt"

func main() {
	dividedby := 1.0
	s := 0.0
	for i := 1.0; i <= 39.0; {
		s += i / dividedby

		i += 2
		dividedby *= 2
	}
	fmt.Println(s)
}
