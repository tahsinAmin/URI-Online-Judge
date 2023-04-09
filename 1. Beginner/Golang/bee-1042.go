package main

import (
	"fmt"
	"sort"
)

func main() {
	var a, b, c int
	fmt.Scanf("%v %v %v", &a, &b, &c)
	arr := []int{a, b, c}
	sort.Ints(arr)

	for _, item := range arr {
		fmt.Println(item)
	}
	fmt.Println()
	fmt.Printf("%d\n%d\n%d\n", a, b, c)
}