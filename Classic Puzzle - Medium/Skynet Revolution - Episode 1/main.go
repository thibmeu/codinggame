package main

import "fmt"
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	// N: the total number of nodes in the level, including the gateways
	// L: the number of links
	// E: the number of exit gateways
	var N, L, E int
	fmt.Scan(&N, &L, &E)

	for i := 0; i < L; i++ {
		// N1: N1 and N2 defines a link between these nodes
		var N1, N2 int
		fmt.Scan(&N1, &N2)
	}
	for i := 0; i < E; i++ {
		// EI: the index of a gateway node
		var EI int
		fmt.Scan(&EI)
	}
	for {
		// SI: The index of the node on which the Skynet agent is positioned this turn
		var SI int
		fmt.Scan(&SI)


		// fmt.Fprintln(os.Stderr, "Debug messages...")

		// Example: 0 1 are the indices of the nodes you wish to sever the link between
		fmt.Println("0 1")
	}
}