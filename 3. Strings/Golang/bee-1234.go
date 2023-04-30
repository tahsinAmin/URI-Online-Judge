package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() != false {
		str := scanner.Text()
		var newStr string
		flag := true

		for _, s := range str {
			if string(s) == " " {
				newStr += " "
			} else {
				if flag {
					newStr += strings.ToUpper(string(s))
				} else {
					newStr += strings.ToLower(string(s))
				}
				flag = !flag
			}
		}
		fmt.Println(newStr)
	}
}
