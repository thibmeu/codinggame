package main

import "fmt"
//import "os"

/**
 * The while loop represents the game.
 * Each iteration represents a turn of the game
 * where you are given inputs (the heights of the mountains)
 * and where you have to print an output (the index of the mountain to fire on)
 * The inputs you are given are automatically updated according to your last actions.
 **/

func main() {
	for {
		var iMax, curMax int
		for i := 0; i < 8; i++ {
			// mountainH: represents the height of one mountain.
			var mountainH int
			fmt.Scan(&mountainH)
			if mountainH > curMax {
				iMax = i
				curMax = mountainH
			}
		}

		// fmt.Fprintln(os.Stderr, "Debug messages...")
		fmt.Println(iMax) // The index of the mountain to fire on.
	}
}