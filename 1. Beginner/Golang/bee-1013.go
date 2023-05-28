package main

import (
	"fmt"
	"math"
)

func main() {
	var a,b,c int

	fmt.Scanln(&a,&b,&c)
	res := (a + b + math.abs(a-b))/2
	greatest = math.max(res, c)
	fmt.Println(greatest + "eh o maior");

}