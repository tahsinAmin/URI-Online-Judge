package main

import (
	"fmt"
)

func main() {
	notes := [3]int{3600,60,1}
	val :=[3]int{0,0,0}

	var remains int
	fmt.Scan(&remains)
	for i:= 0; i < 3; i++ {
		if remains >= notes[i] {
			val[i] = remains / notes[i]
			remains = remains % notes[i]
		}
	}
	fmt.Printf("%d:%d:%d\n", val[0],val[1],val[2]);
}