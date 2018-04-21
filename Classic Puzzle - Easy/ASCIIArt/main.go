package main

import "fmt"
import "os"
import "bufio"
import "strings"
//import "strings"
//import "strconv"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	var L int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&L)

	var H int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&H)

	const maxH = 30
	scanner.Scan()
	text := scanner.Text()
	var alphabet [27][maxH]string
	for i := 0; i < H; i++ {
		scanner.Scan()
		row := scanner.Text()
		iLettre := 0
		c := 0
		for _, char := range row {
			if (c == L) {
				iLettre++
				c = 0
			}
			c++
			alphabet[iLettre][i] += string(char)
		}
	}


	var result [maxH]string
	for _, letter := range text {
		iLetter := int(strings.ToUpper(string(letter))[0])-int('A')
		if iLetter < 0 || iLetter >= 26 {
			iLetter = 26
		}
		for i := 0; i < H; i++ {
			result[i] += alphabet[iLetter][i]
		}
	}

	// fmt.Fprintln(os.Stderr, "Debug messages...")
	for i := 0; i < H; i++ {
		fmt.Println(result[i])
	}
}