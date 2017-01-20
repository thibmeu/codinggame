package main

import "fmt"
import "os"
import "bufio"
import "strings"
//import "strconv"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	// N: Number of elements which make up the association table.
	var N int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&N)

	// Q: Number Q of file names to be analyzed.
	var Q int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&Q)

	association := make(map[string]string)
	for i := 0; i < N; i++ {
		// EXT: file extension
		// MT: MIME type.
		var EXT, MT string
		scanner.Scan()
		fmt.Sscan(scanner.Text(),&EXT, &MT)

		association[strings.ToLower(EXT)] = MT
	}
	for i := 0; i < Q; i++ {
		scanner.Scan()
		FNAME := scanner.Text() // One file name per line.

		a := strings.Split(FNAME, ".")
		EXT := strings.Trim(a[len(a)-1], ".")

		if val, ok := association[strings.ToLower(EXT)]; ok && len(a) != 1 {
			fmt.Println(val)
		} else {
			fmt.Println("UNKNOWN")
		}
	}

}