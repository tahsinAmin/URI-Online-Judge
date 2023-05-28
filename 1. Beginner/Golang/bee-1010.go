package main
import "fmt"
func main() {
	var a, b, c, sm float64
	for i:=0; i< 2; i++ {
		fmt.Scan(&a, &b, &c)
		sm += b*c
	}
    fmt.Printf("VALOR A PAGAR: R$ %.2f\n", sm)    
}