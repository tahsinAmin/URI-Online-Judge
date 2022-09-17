package main

import (
	"fmt"
)

func main() {
	var (
		cases, team1, team1_, team2, team2_ int
		unused                              string
	)
	fmt.Scan(&cases)
	for ; cases > 0; cases-- {
		fmt.Scan(&team1, &unused, &team2)
		fmt.Scan(&team2_, &unused, &team1_)

		if team1+team1_ > team2+team2_ {
			fmt.Println("Time 1")
		} else if team2+team2_ > team1+team1_ {
			fmt.Println("Time 2")
		} else {
			if team2 > team1_ {
				fmt.Println("Time 2")
			} else if team1_ > team2 {
				fmt.Println("Time 1")
			} else {
				fmt.Println("Penaltis")
			}
		}
	}
}
