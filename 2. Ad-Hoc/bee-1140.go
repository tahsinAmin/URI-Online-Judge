// Learned
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var s []string
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		r := scanner.Text()
		if r[0] == 42 {
			break
		}
		tautogram := strings.ToLower(r[0:1])
		s = strings.Split(r, " ")
		flag := 1
		for i := 0; i < len(s); i++ {
			if tautogram != strings.ToLower(s[i][0:1]) {
				flag = 0
				break
			}
		}
		if flag == 1 {
			fmt.Println("Y")
		} else {
			fmt.Println("N")
		}
	}
}
