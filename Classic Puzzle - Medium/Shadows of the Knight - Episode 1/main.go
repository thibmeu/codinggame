package main

import "fmt"
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	// W: width of the building.
	// H: height of the building.
	var W, H int
	fmt.Scan(&W, &H)

	// N: maximum number of turns before game over.
	var N int
	fmt.Scan(&N)

	var X0, Y0 int
	fmt.Scan(&X0, &Y0)

	minX, maxX, minY, maxY := 0, W, 0, H
	x, y := X0, Y0
	for {
		// bombDir: the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
		var bombDir string
		fmt.Scan(&bombDir)


		switch bombDir {
		case "U":
			minX, maxX = x, x+1
			maxY = y-1
		case "UR":
			minX = x+1
			maxY = y
		case "R":
			minX = x+1
			minY, maxY = y, y+1
		case "DR":
			minX = x+1
			minY = y+1
		case "D":
			minX, maxX = x, x+1
			minY = y+1
		case "DL":
			maxX = x
			minY = y+1
		case "L":
			maxX = x
			minY, maxY = y, y+1
		case "UL":
			maxX = x
			maxY = y
		}

		x = (minX+maxX)/2
		y = (minY+maxY)/2

		// the location of the next window Batman should jump to.
		fmt.Println(x, y)
	}
}