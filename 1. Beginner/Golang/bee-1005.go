package main
import "fmt"

func main() {
	var a, b float64
	fmt.Scan(&a, &b)
	fmt.Printf("MEDIA = %.1f\n", ((a*3.5) + (b*7.5))/ 11.0)    
}