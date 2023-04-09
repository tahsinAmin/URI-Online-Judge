package main

import "fmt"

func main() {

	var experiments = map[string]float32{"S": 0, "R": 0, "C": 0}
	var (
		total, val float32
		num        int
		line       string
	)

	fmt.Scan(&num)
	for i := 0; i < num; i++ {
		fmt.Scan(&val, &line)
		total += val
		experiments[line] += val
	}
	fmt.Printf("Total: %.0f cobaias\n", total)
	fmt.Printf("Total de coelhos: %.0f\n", experiments["C"])
	fmt.Printf("Total de ratos: %.0f\n", experiments["R"])
	fmt.Printf("Total de sapos: %.0f\n", experiments["S"])
	fmt.Printf("Percentual de coelhos: %.2f %%\n", experiments["C"]/total*100)
	fmt.Printf("Percentual de ratos: %.2f %%\n", experiments["R"]/total*100)
	fmt.Printf("Percentual de sapos: %.2f %%\n", experiments["S"]/total*100)
}
