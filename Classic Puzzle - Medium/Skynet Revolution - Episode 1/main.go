package main

import (
	"fmt"
)
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

type rank int

const (
	NORMAL rank = iota
	GATEWAY rank = iota
	SKYNET = iota
)

type link int
const (
	NONE = iota
	LINK link = iota
	BROKEN = iota
)

type node struct {
	number int
	r rank
}

type graph struct {
	nodes    [][]link
	gateways map[int]rank
}

func (g *graph) init(N int) {
	*g =  graph{nodes: make([][]link, N), gateways: make(map[int]rank)}

	for i := 0; i < N; i++ {
		g.nodes[i] = make([]link, N)
	}
}

func (g *graph) add(a, b int, l link) {
	g.nodes[a][b] = l
	g.nodes[b][a] = l
}

func (g *graph) remove(a, b int) {
	g.add(a, b, BROKEN)
	g.add(b, a, BROKEN)
}

func (g *graph) grant(a int, r rank) {
	g.gateways[a] = r
}

func (g graph) neighbours(a int) []int {
	result := make([]int, 0)
	for i, l := range g.nodes[a] {
		if l == LINK {
			result = append(result, i)
		}
	}
	return result
}

func (g graph) ranks() ([]int, int) {
	gateways := make([]int, 0)
	var skynet int
	for i, r := range g.gateways {
		if r == GATEWAY {
			gateways = append(gateways, i)
		} else if r == SKYNET {
			skynet = i
		}
	}
	return gateways, skynet
}

func (g graph) isGateway(a int) bool {
	return g.gateways[a] == GATEWAY
}

func (g graph) bfs(start, end int) (int, int, int) {
	dist, a, b := 0, 0, 0

	dejaVu := make([]bool, len(g.nodes))
	// Compute minimum distance between start and end
	queue := make([]int, 0)
	queue = append(queue, start, 0, 0)

	for len(queue) != 0 {
		a, b, dist := queue[0], queue[1], queue[2]
		dejaVu[a] = true

		//fmt.Println(g.neighbours(a), dejaVu, a)

		if g.isGateway(a) {
			if a > b {
				a, b = b, a
			}
			return dist, a, b
		}
		for _, n := range g.neighbours(a) {
			if dejaVu[n] == false {
				queue = append(queue, n, a, dist+1)
			}
		}

		queue = queue[3:]
	}

	return dist, a, b
}

func weakLink(g graph) (int, int) {
	gateways, skynet := g.ranks()
	minDist, minA, minB := 1000*1000*1000, skynet, gateways[0]

	for _, gateway := range gateways {
		if dist, a, b := g.bfs(skynet, gateway); dist < minDist {
			minDist, minA, minB = dist, a, b
		}
	}

	return minA, minB
}

func main() {
	// N: the total number of nodes in the level, including the gateways
	// L: the number of links
	// E: the number of exit gateways
	var N, L, E int
	fmt.Scan(&N, &L, &E)

	// g: the current graph
	var g graph
	g.init(N)

	for i := 0; i < L; i++ {
		// N1: N1 and N2 defines a link between these nodes
		var N1, N2 int
		fmt.Scan(&N1, &N2)
		g.add(N1, N2, LINK)
	}
	for i := 0; i < E; i++ {
		// EI: the index of a gateway node
		var EI int
		fmt.Scan(&EI)
		g.grant(EI, GATEWAY)
	}
	for {
		// SI: The index of the node on which the Skynet agent is positioned this turn
		var SI int
		fmt.Scan(&SI)
		g.grant(SI, SKYNET)

		weakA, weakB := weakLink(g)
		fmt.Println(weakA, weakB)
		g.remove(weakA, weakB)

		g.grant(SI, NORMAL)
	}
}