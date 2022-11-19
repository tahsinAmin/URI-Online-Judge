# I have leanred

# Character Reead

```
	s := "tahsin"
	fmt.Println(string([]rune(s)[1]))
```

## End of File

```
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() != false {
```

## Iterate

```
		for _, s := range str {
			...
		}
```

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

`fmt.Printf("Area = %.1f\n", (0.5 * (A + B) * C)) `

- For integer

`fmt.Printf("You have %d \n", C)` or `fmt.Printf("You have %.0f \n", C)`

- For Printing '%'
  `fmt.Printf("Percentual de sapos: %.2f %%\n", experiments["S"]/total*100)`

## Scan Format

- bufio (To read a sentence)

```
	scanner := bufio.NewScanner(os.Stdin)
		for scanner.Scan() {
```

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

- Default value

`var num float32; // means num is 0.0`

### Incremenet

` cnt++`
or
`cnt+=1`
