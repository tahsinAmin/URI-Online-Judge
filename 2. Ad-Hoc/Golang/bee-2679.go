package main

import "fmt"

func main()  {
	var x int

	fmt.Scan(&x);
	if (x+1) % 2 {
		fmt.Println(x+2)
	}else {
		fmt.Println(x+1)
	}
}