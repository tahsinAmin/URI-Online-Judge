package main
import "fmt"
func main() {
    var a float64
    const pi = 3.14159

    fmt.Scanln(&a)
    
    fmt.Printf("VOLUME = %.3f\n", (4.0/3.0) * pi * a*a*a)
    
}