package main

import "fmt"

func main() {
	var x, y, z int

	fmt.Scanln(&x, &y, &z)
	for x != 0 {
		result := (x * y * z) / (z - x)
		fmt.Print(result)
		if result == 1 {
			fmt.Println(" pagina")
		} else {
			fmt.Println(" paginas")
		}
		fmt.Scanln(&x, &y, &z)
	}
}
