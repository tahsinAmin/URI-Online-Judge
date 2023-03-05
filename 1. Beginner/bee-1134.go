package main

import "fmt"

func main () {
    readNum := 0
    fuel := map[int]int{1: 0, 2: 0, 3: 0}

    for true {
        fmt.Scanf("%d", &readNum)
        if readNum == 4 {break}
        if _, ok := fuel[readNum]; ok {
            fuel[readNum] += 1
        }    
    } 

    fmt.Printf("MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d\n", fuel[1], fuel[2], fuel[3])
}