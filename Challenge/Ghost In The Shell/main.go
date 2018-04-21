package main

import "fmt"
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

type factory struct {
	player int
	cyborg int
	production int
}

type troop struct {
	player int
	start int
	end int
	cyborg int
	turns int
}

type graph struct {
	link [][]int
}

func (g *graph) Add(a, b, dist int) {
	if g.link[a] == nil {
		g.link[a] = make([]int, len(g.link))
	}
	if g.link[b] == nil {
		g.link[b] = make([]int, len(g.link))
	}
	g.link[a][b] = dist
	g.link[b][a] = dist
}

func (g * graph) Remove(a, b int) {
	g.link[a][b] = nil
	g.link[b][a] = nil
}

func (g graph) Dist(a, b int) int {
	return g.link[a][b]
}

func main() {
	// factoryCount: the number of factories
	var factoryCount int
	fmt.Scan(&factoryCount)

	factories := make([] factory, factoryCount)
	distances := graph{make([][] int, factoryCount)}

	// linkCount: the number of links between factories
	var linkCount int
	fmt.Scan(&linkCount)

	for i := 0; i < linkCount; i++ {
		var factory1, factory2, distance int
		fmt.Scan(&factory1, &factory2, &distance)
		distances.Add(factory1, factory2, distance)
	}
	for {
		// entityCount: the number of entities (e.g. factories and troops)
		var entityCount int
		fmt.Scan(&entityCount)

		troops := make([]troop, 0)
		for i := 0; i < entityCount; i++ {
			var entityId int
			var entityType string
			var arg1, arg2, arg3, arg4, arg5 int
			fmt.Scan(&entityId, &entityType, &arg1, &arg2, &arg3, &arg4, &arg5)

			switch entityType {
			case "FACTORY":
				factories[entityId] = factory{arg1, arg2, arg3}
				break
			case "TROOP":
				troops = append(troops, troop{arg1, arg2, arg3, arg4, arg5})
				break
			}
		}

		// fmt.Fprintln(os.Stderr, "Debug messages...")

		// Any valid action, such as "WAIT" or "MOVE source destination cyborgs"
		fmt.Println("WAIT")
	}
}