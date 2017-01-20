package main

import "fmt"
import "sort"
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	var N int
	fmt.Scan(&N)

	horses := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&(horses[i]))
	}

	sort.Ints(horses)

	minD := 10*1000*1000
	for i := 0; i < N-1; i++ {
		if dist := horses[i+1]-horses[i]; dist < minD {
			minD = dist
		}
	}
	// fmt.Fprintln(os.Stderr, "Debug messages...")
	fmt.Println(minD)// Write answer to stdout
}