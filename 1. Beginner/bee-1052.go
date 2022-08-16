package main

import "fmt"

func main() {
	var n int
	var arr = []string{"", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}
	fmt.Scan(&n)
	fmt.Println(arr[n])
}
