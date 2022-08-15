package main

import "fmt"

func main() {
	var s, t, u string
	fmt.Scan(&s, &t, &u)

	if s == "vertebrado" {
		if t == "ave" {
			if u == "carnivoro" {
				fmt.Println("aguia")
			} else {
				fmt.Println("pomba")
			}
		} else {
			if u == "onivoro" {
				fmt.Println("homem")
			} else {
				fmt.Println("vaca")
			}
		}
	} else if s == "invertebrado" {
		if t == "inseto" {
			if u == "hematofago" {
				fmt.Println("pulga")

			} else {
				fmt.Println("lagarta")
			}
		} else {
			if u == "hematofago" {
				fmt.Println("sanguessuga")
			} else {
				fmt.Println("minhoca")
			}
		}
	}
}
