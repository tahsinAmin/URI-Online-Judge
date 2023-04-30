package main

import (
	"fmt"
)

func main() {
    
    var A, B, C, D int
    fmt.Scanf("%v %v %v %v", &A, &B, &C, &D)
    
    if B > C && D > A && (C + D) > (A + B) && (C > 0 && D > 0) && A%2 == 0 {
        fmt.Println("Valores aceitos");
    } else {
        fmt.Println("Valores nao aceitos"); 
    }
}