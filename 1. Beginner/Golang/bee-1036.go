package main

import (
	"fmt"
	"math"
)

func main() {
    
    var a,b,c float64
    fmt.Scanf("%v %v %v", &a, &b, &c)
    
    if a == 0 || (math.Pow(b,2)- 4*a*c < 0) {
        fmt.Println("Impossivel calcular")    
    }else {
        r1:=( (-b + math.Sqrt(math.Pow(b,2)- 4*a*c))/(2*a))
        r2:=( (-b - math.Sqrt(math.Pow(b,2)- 4*a*c))/(2*a))
        fmt.Printf("R1 = %.5f\nR2 = %.5f\n", r1, r2)
    }
}