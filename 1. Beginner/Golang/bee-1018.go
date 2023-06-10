package main

import (
	"fmt"
)

func main() {
	notes := [7]int{100,50,20,10,5,2,1}
	var remains int
	fmt.Scan(&remains)
	fmt.Println(remains)
	for i:= 0; i < 7; i++ {
		y := 0
		if remains >= notes[i] {
			y = remains / notes[i]
			remains = remains % notes[i]
		}
		fmt.Printf("%d nota(s) de R$ %d,00\n", y, notes[i]);
	}
}