package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var (
		n, m      int
		rangeFlag bool
	)
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Scan(&n, &m)
	a := make([][]string, 0)
	rangeFlag = true
	for i := 0; i < n; i++ {
		scanner.Scan()
		str := scanner.Text()
		splitB := strings.Split(str, " ")
		a = append(a, splitB)
	}
	k, l := 0, 0
	if rangeFlag {
		cnt := 0
		for i := 1; i < n-1; i++ {
			for j := 1; j < m-1; j++ {
				if a[i][j] == "42" {
					if a[i-1][j-1] == "7" && a[i-1][j] == "7" && a[i-1][j+1] == "7" && a[i][j-1] == "7" && a[i][j+1] == "7" && a[i+1][j-1] == "7" && a[i+1][j] == "7" && a[i+1][j+1] == "7" {
						cnt, k, l = 1, i, j
						break
					}
				}
			}
		}
		if cnt == 0 {
			fmt.Println("0 0")
		} else {
			fmt.Println((k + 1), (l + 1))
		}
	}
}
