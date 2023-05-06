package main

import "fmt"

func main()  {
	for i := 0; i < 7; i++ {
		if i == 0 || i == 6 {
			fmt.Println("---------------------------------------");
		} else {
			fmt.Println("|                                     |");
		}
	}
}