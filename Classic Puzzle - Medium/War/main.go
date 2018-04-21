package main

import (
	"fmt"
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

func battle(p1, p2 *[]card, i int) (int, int) {
	if i >= len(*p1) {
		return -1, len(*p1)-1
	} else if i >= len(*p2) {
		return -1, len(*p2)-1
	}
	c1, c2 := (*p1)[i], (*p2)[i]

	var player int
	if c1.r == c2.r {

		var iEnd int
		player, iEnd = battle(p1, p2, i+4)
		if i != 0 {
			return player, iEnd
		} else {
			if player == 1 {
				*p1 = append(*p1, (*p1)[:iEnd+1]...)
				*p1 = append(*p1, (*p2)[:iEnd+1]...)
			} else if player == 2 {
				*p2 = append(*p2, (*p1)[:iEnd+1]...)
				*p2 = append(*p2, (*p2)[:iEnd+1]...)
			}
			*p1 = (*p1)[iEnd+1:]
			*p2 = (*p2)[iEnd+1:]
		}
	} else {
		if c1.r > c2.r {
			player = 1
		} else {
			player = 2
		}
		if i == 0 {
			if player == 1 {
				*p1 = append(*p1, c1, c2)
			} else {
				*p2 = append(*p2, c1, c2)
			}
			*p1 = (*p1)[1:]
			*p2 = (*p2)[1:]
		}
	}
	return player, i
}

func main() {

	cards := make([][]card, 2)
	for player := 0; player < 2; player++ {
		// n: the number of cards for player
		var n int
		fmt.Scan(&n)
		cards[player] = make([]card, n)

		for i := 0; i < n; i++ {
			// cardp: the n cards of player
			var cardp string
			fmt.Scan(&cardp)

			var r rank
			switch cardp[0] {
			case '1':
				r = 1
				if cardp[1] == '0' {
					r = 10
				}
			case 'J':
				r = 11
			case 'Q':
				r = 12
			case 'K':
				r = 13
			case 'A':
				r = 14
			default:
				j, _ := strconv.Atoi(string(cardp[0]))
				r = rank(j)
			}

			var s suit
			switch cardp[len(cardp)-1] {
			case 'H':
				s = HEART
			case 'D':
				s = DIAMOND
			case 'C':
				s = CLUB
			case 'S':
				s = SPADE
			default:
				s = -1
			}

			cards[player][i] = card{r, s}
		}
	}

	turn, player := 0, 0
	for len(cards[0]) > 0 && len(cards[1]) > 0 {
		player, _ = battle(&cards[0], &cards[1], 0)
		turn++
	}

	switch player {
	case -1:
		fmt.Println("PAT")
	default:
		fmt.Println(player, turn);
	}
}