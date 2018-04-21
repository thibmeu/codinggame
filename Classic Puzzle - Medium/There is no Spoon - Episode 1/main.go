package main

import "fmt"
import "os"
import "bufio"
//import "strings"
//import "strconv"

/**
 * Don't let the machines win. You are humanity's last hope...
 **/

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	// width: the number of cells on the X axis
	var width int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&width)

	// height: the number of cells on the Y axis
	var height int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&height)

	car := make([][]bool, height)
	for i := 0; i < height; i++ {
		scanner.Scan()
		line := scanner.Text() // width characters, each either 0 or .
		row := make([]bool, width)
		for iChar, char := range line {
			row[iChar] = (string(char) == "0")
		}
		car[i] = row
	}

	for i, row := range car {
		for j, node := range row {
			if node {
				fmt.Print(j, i, " ")
				isNeigh := false
				for k := j+1; k < width; k++ {
					if car[i][k] {
						fmt.Print(k, i, " ")
						isNeigh = true
						break
					}
				}
				if !isNeigh {
					fmt.Print(-1, -1, " ")
				}
				isNeigh = false
				for k := i+1; k < height; k++ {
					if car[k][j] {
						fmt.Println(j, k)
						isNeigh = true
						break
					}
				}
				if !isNeigh {
					fmt.Println(-1, -1)
				}
			}
		}
	}

}