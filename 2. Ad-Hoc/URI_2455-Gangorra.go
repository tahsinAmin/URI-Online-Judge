import "fmt"
package main


func main() {
    var p1, c1, p2, c2 int
    fmt.Scan( & p1, & c1, & p2, & c2)
    left := p1*c1
    right := p2*c2
    if left > right {
        fmt.Println(-1)
    }else if left == right {
        fmt.Println(0)
    }else {
        fmt.Println(1)
    }
}
