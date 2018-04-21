package main

import "fmt"
import "os"
import "bufio"
//import "strings"
//import "strconv"

func charToEncoded(char rune, result *string, prec *byte) {

	for i:=1; i<8; i++ {
		b := (byte(char) << byte(i)) >> byte(7)
		if b == *prec {
			*result += "0"
		} else {
			if (len(*result) != 0) {
				*result += " "
			}
			if (b == 0) {
				*result += "00 0"
			} else {
				*result += "0 0"
			}
			*prec = b
		}
	}

}

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	scanner.Scan()
	message := scanner.Text()

	//fmt.Println(message)
	var result string

	prec := byte(2)
	for _, char := range message {
		charToEncoded(char, &result, &prec)
	}

	// fmt.Fprintln(os.Stderr, "Debug messages...")
	fmt.Println(result)// Write answer to stdout
}