package main

import "fmt"
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

func main() {
	// lightX: the X position of the light of power
	// lightY: the Y position of the light of power
	// initialTX: Thor's starting X position
	// initialTY: Thor's starting Y position
	var lightX, lightY, initialTX, initialTY int
	fmt.Scan(&lightX, &lightY, &initialTX, &initialTY)

	x := initialTX
	y := initialTY

	for {
		// remainingTurns: The remaining amount of turns Thor can move. Do not remove this line.
		var remainingTurns int
		fmt.Scan(&remainingTurns)

		// A single line providing the move to be made: N NE E SE S SW W or NW
		dx := lightX-x
		dy := lightY-y

		if dx == 0 {
			if dy < 0 {
				fmt.Println("N")
				y--
			} else {
				fmt.Println("S")
				y++
			}
		} else if dy == 0 {
			if dx < 0 {
				fmt.Println("W")
				x--
			} else {
				fmt.Println("E")
				x++
			}
		} else if dy < 0 {
			y--
			if dx < 0 {
				fmt.Println("NW")
				x--
			} else {
				fmt.Println("NE")
				x--
			}
		} else {
			y++
			if dx < 0 {
				fmt.Println("SW")
				x--
			} else {
				fmt.Println("SE")
				x++
			}
		}
	}
}