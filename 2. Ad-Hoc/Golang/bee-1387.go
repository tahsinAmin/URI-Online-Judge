package main

import "fmt"

func main() {
	var left, right int
	for {
		fmt.Scanf("%d %d", &left, &right)
		if left == 0 && right == 0 {
			break
		}
		fmt.Println(left + right)
	}
}
