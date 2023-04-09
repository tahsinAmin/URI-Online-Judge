package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() != false {
		str := scanner.Text()
		if str == "direita" {
			fmt.Println("frances")
		} else if str == "nenhuma" {
			fmt.Println("portugues")
		} else if str == "esquerda" {
			fmt.Println("ingles")
		} else {
			fmt.Println("caiu")
		}
	}
}
