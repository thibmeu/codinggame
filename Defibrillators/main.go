package main

import "fmt"
import "os"
import "bufio"
import "strings"
import "math"
import "strconv"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func stringToFloat(s string) float64 {
	r, _ := strconv.ParseFloat(strings.Replace(s, ",", ".", -1), 64)
	return r
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	var LON string
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&LON)
	lon := stringToFloat(LON)
	lon *= math.Pi/180

	var LAT string
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&LAT)
	lat := stringToFloat(LAT)
	lat *= math.Pi/180

	var N int
	scanner.Scan()
	fmt.Sscan(scanner.Text(),&N)

	best := ""
	minDist := 1000*1000*1000.0
	for i := 0; i < N; i++ {
		scanner.Scan()
		DEFIB := scanner.Text()
		descr := strings.Split(DEFIB, ";")
		nom := strings.Trim(descr[1], ";")
		xD := stringToFloat(strings.Trim(descr[4], ";"))
		xD *= math.Pi/180
		yD := stringToFloat(strings.Trim(descr[5], ";"))
		yD *= math.Pi/180
		x := (xD - lon)*math.Cos((yD+lat)/2)
		y := yD - lat
		if dist := math.Sqrt(x*x+y*y); dist < minDist {
			minDist = dist
			best = nom
		}
	}

	// fmt.Fprintln(os.Stderr, "Debug messages...")
	fmt.Println(best)// Write answer to stdout
}