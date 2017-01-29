package main

import (
	"fmt"
	//"os"
	"strconv"
)

type rank int

type suit int
const (
	HEART suit = iota
	DIAMOND = iota
	CLUB = iota
	SPADE = iota
)

type card struct {
	r rank
	s suit
}

func main() {

	cards := make([][]card, 2)
	for player := 0; player < 2; player++ {
		// n: the number of cards for player
		var n int
		fmt.Scan(&n)

		for i := 0; i < n; i++ {
			cards[player] = make([]card, n)
			// cardp: the n cards of player
			var cardp string
			fmt.Scan(&cardp)

			var r rank
			switch strr := cardp[0] {
			case cardp[1] == '0':
				r = 10
			case "J":
				r = 11
			case "Q":
				r = 12
			case "K":
				r = 13
			case "A":
				r = 14
			default:
				strconv.Atoi(string(strr))
			}

			var s suit
			switch cardp[len(cardp)-1] {
			case "H":
				s = HEART
			case "D":
				s = DIAMOND
			case "C":
				s = CLUB
			case "S":
				s = SPADE
			}

			cards[player][i] = card{r, s}
		}
	}

	//fmt.Fprintln(os.Stderr, "Debug messages...")
	fmt.Println("PAT")// Write answer to stdout
}