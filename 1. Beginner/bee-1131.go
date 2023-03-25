package main

import "fmt"

func main () {
	var inter, gremio, empates, x, y int
	opt, n:= 1, 0

	for {
		fmt.Scan(&x)
		fmt.Scan(&y)
		n+=1

		if x > y {
			inter+=1
		} else if y > x {
			gremio+=1
		} else {
			empates+=1
		}

		for ;n>=0; {
			fmt.Println("Novo grenal (1-sim 2-nao)");
			fmt.Scan(&opt)
			if opt == 1 || opt ==2 {
				break
			}
		}
		if opt != 1 {
			break
		}
	}
	fmt.Println(n, "grenais");
	fmt.Printf("Inter:%d\nGremio:%d\nEmpates:%d\n", inter, gremio, empates)
	if inter > gremio {
		fmt.Println("Inter venceu mais")
	} else if gremio > inter {
		fmt.Println("Gremio venceu mais")
	} else {
		fmt.Println("Não houve vencedor")
	}
}