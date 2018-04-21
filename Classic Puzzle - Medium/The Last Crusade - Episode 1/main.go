package main

import "fmt"
import "os"
import (
	"bufio"
	"encoding/json"
	"regexp"
)
//import "strings"
//import "strconv"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	// W: number of columns.
	// H: number of rows.
	var W, H int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&W, &H)

	for i := 0; i < H; i++ {
		scanner.Scan()
		LINE := scanner.Text() // represents a line in the grid and contains W integers. Each integer represents one room of a given type.
		re := regexp.MustCompile(" ")
		str := "[" + re.ReplaceAllString(LINE, ",") + "]"
		var ints []int
		json.Unmarshal([]byte(str), &ints)

	}
	// EX: the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
	var EX int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&EX)

	for {
		var XI, YI int
		var POS string
		scanner.Scan()
		fmt.Sscan(scanner.Text(),&XI, &YI, &POS)


		// fmt.Fprintln(os.Stderr, "Debug messages...")

		// One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
		fmt.Println("0 0")
	}
}