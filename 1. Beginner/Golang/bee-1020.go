package main

import (
	"fmt"
)

func main() {
	notes := [3]int{365,30,1}
	val :=[3]int{0,0,0}

	var remains int
	fmt.Scan(&remains)
	for i:= 0; i < 3; i++ {
		if remains >= notes[i] {
			val[i] = remains / notes[i]
			remains = remains % notes[i]
		}
	}
	fmt.Printf("%d ano(s)\n%d mes(es)\n%d mes(es)\n", val[0],val[1],val[2]);
}