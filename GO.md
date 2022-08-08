# I have leanred

## Package

- math package

```
package main

import (
	"math"
)

func main() {
  ...
  r1:=( (-b + math.Sqrt(math.Pow(b,2)- 4*a*c))/(2*a))
}
```

## Print format

- To 1 decimal place

`fmt.Printf("Area = %.1f\n", (0.5 * (A + B) * C))
`

- For integer

`fmt.Printf("O JOGO DUROU %d HORA(S)\n", C)`

## Scan Format

- Scanf vs. Scan

ScanF

```
	var x, y int
	fmt.Scanf("%v %v", &x, &y)
```

Scan

```
	var x, y int
	fmt.Scan(&x, &y)
```

## Slice

- List sort descending

```
	lados := []float64{A, B, C}

	sort.Slice(lados, func(i, j int) bool { // Descending order slice
		return lados[i] > lados[j]
	})
```

## Variables

- Declaring multiple variable at once

`A, B, C = arr[0], arr[1], arr[2]`
