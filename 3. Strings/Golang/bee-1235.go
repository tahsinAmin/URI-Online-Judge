package main

import (
	"bufio"
	"fmt"
	"os"
)

func reverse(str string) (result string) {
	for _, v := range str {
		result = string(v) + result
	}
	return
}

func main() {
	var (
		n int
	)
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		scanner.Scan()
		str := scanner.Text()
		strRev := reverse(str)
		len_s, len_half := len(strRev), 0
		if len_s%2 == 0 {
			len_half = len_s / 2
		} else {
			len_half = len_s/2 + 1
		}
		fmt.Println(strRev[len_half:] + "" + strRev[:len_half])
	}
}
