package main
import "fmt"

func main() {
	var a, b float64
	st := ""
	fmt.Scan(&st,&a, &b)

	a = a + (b*0.15)
    fmt.Printf("TOTAL = R$ %.2f\n", a)    
}