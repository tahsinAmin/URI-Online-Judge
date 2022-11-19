package main

import "fmt"

func main() {
	var (
		n       int
		pokemon string
	)
	set := map[string]int{}
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&pokemon)
		_, ok := set[pokemon]
		if !ok {
			set[pokemon] = 1
		}
	}
	fmt.Printf("Falta(m) %d pomekon(s).\n", (151 - len(set)))
}
