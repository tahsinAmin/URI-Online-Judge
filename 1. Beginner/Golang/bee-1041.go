package main

import (
	"fmt"
)

func main() {
	var x, y float64
	fmt.Scanf("%v %v", &x, &y)

	if x == 0 || y == 0 {
		if x == 0  && y == 0 {
			fmt.Println("Origem"); 
		} else if x == 0  && y != 0 {
			fmt.Println("Eixo Y");
		} else {
			fmt.Println("Eixo X");
		}
	} else {
		if(x > 0  && y > 0) {
			fmt.Println("Q1")
		} else if(x > 0  && y < 0) {
			fmt.Println("Q4")
		} else if(x < 0  && y > 0) {
			fmt.Println("Q2")
		} else {
			fmt.Println("Q3")
		}
	}
}