package main

import (
	"fmt"
	"os"
)

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

	minX, maxX := 0, W-1
	minY, maxY := 0, H-1
	mX, mY := 0, 0
	x, y := X0, Y0
	line := minX == maxX
	for {
		// bombDir: Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
		var bombDir string
		fmt.Scan(&bombDir)

		fmt.Fprintln(os.Stderr, bombDir)

		addX, addY := 0, 0
		if x == mX && (maxX-minX)%2 == 1 {
			addX = 1
		}
		if y == mY && (maxY-minY)%2 == 1 {
			addY = 1
		}

		switch bombDir {
		case "COLDER":
			if !line {
				if x > mX {
					maxX = mX-addX
				} else {
					minX = mX+addX
				}
			} else {
				if y > mY {
					maxY = mY-addY
				} else {
					minY = mY+addY
				}
			}
			break
		case "WARMER":
			if !line {
				if x < mX {
					maxX = mX-addX
				} else {
					minX = mX+addX
				}
			} else {
				if y < mY {
					maxY = mY-addY
				} else {
					// On passe ici
					minY = mY+addY
				}
			}
			break
		case "SAME":
			if !line {
				if minX == maxX {
					line = true
				} else {
					minX = mX
					maxX = mX
				}
			} else {
				if minY == maxY {
					break
				} else {
					minY = mY
					maxY = mY
				}
			}
			break
		case "UNKOWN":
			break
		}

		mX = (minX + maxX) / 2
		mY = (minY + maxY) / 2

		fmt.Fprintln(os.Stderr, "[", minX, maxX,"]", x)
		fmt.Fprintln(os.Stderr, "[", minY, maxY,"]", y)

		xP := x
		x =  minX + maxX - x
		y =  minY + maxY - y

		if x == xP && !line {
			x++
			mX = (minX + maxX+1) / 2
		}

		if !line {
			y = Y0
		}

		//fmt.Fprintln(os.Stderr, "-------", x, mX)
		if x < minX {
			mX = (x + maxX) / 2
			x = maxX
		} else if x > maxX {
			mX = (minX + x) / 2
			x = minX
		}
		if y < minY {
			mY = (y + maxY) / 2
			y = maxY
		} else if y > maxY {
			mY = (minY + y) / 2
			y = minY
		}
		fmt.Fprintln(os.Stderr, "Moyenne", mX)
		fmt.Println(x, y)// Write action to stdout
	}
}