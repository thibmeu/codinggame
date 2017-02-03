package main

import "fmt"
import "os"
import "bufio"
import "strings"
import "strconv"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	var n int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&n)

	scanner.Scan()
	inputs := strings.Split(scanner.Text()," ")
	var precMax, loss int64
	for i := 0; i < n; i++ {
		v,_ := strconv.ParseInt(inputs[i],10,32)
		if i == 0 {
			precMax = v
		}

		if v > precMax {
			precMax = v
		}

		if v - precMax < loss {
			loss = v - precMax
		}
	}

	// fmt.Fprintln(os.Stderr, "Debug messages...")
	fmt.Println(loss)// Write answer to stdout
}