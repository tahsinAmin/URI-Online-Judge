package main

import "fmt"

func main() {
	var n, lowNum, lowPos int

	fmt.Scan(&n)
	a := make([]int, n)

	fmt.Scan(&a[0])
	lowNum=a[0]
	lowPos=0

	for i := 1; i < n; i++ {
		fmt.Scan(&a[i])
		if a[i] < lowNum {
			lowNum = a[i]
			lowPos = i
		}
	}
	
	fmt.Println("Menor valor:", lowNum)
	fmt.Println("Posicao:", lowPos)
}
