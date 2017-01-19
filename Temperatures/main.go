package main

import "fmt"
import "os"
import "bufio"
import "math"
import "strconv"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	// n: the number of temperatures to analyse
	var n int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&n)

	result := 10*1000
	for i:=0; i<n; i++ {
		scanner.Scan()
		temp, _ := strconv.Atoi(scanner.Text())
		if math.Abs(float64(temp)) < math.Abs(float64(result)) || (math.Abs(float64(temp)) == math.Abs(float64(result)) && int(temp) > result) {
			result = int(temp)
		}
	}
	//temps := scanner.Text() // the n temperatures expressed as integers ranging from -273 to 5526

	if (n == 0) {
		result = 0
	}
	// fmt.Fprintln(os.Stderr, "Debug messages...")
	fmt.Println(result)// Write answer to stdout
}