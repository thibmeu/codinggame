package main

import "fmt"
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	// nbFloors: number of floors
	// width: width of the area
	// nbRounds: maximum number of rounds
	// exitFloor: floor on which the exit is found
	// exitPos: position of the exit on its floor
	// nbTotalClones: number of generated clones
	// nbAdditionalElevators: ignore (always zero)
	// nbElevators: number of elevators
	var nbFloors, width, nbRounds, exitFloor, exitPos, nbTotalClones, nbAdditionalElevators, nbElevators int
	fmt.Scan(&nbFloors, &width, &nbRounds, &exitFloor, &exitPos, &nbTotalClones, &nbAdditionalElevators, &nbElevators)

	elevators := make([]int, nbFloors)
	for i := 0; i < nbElevators; i++ {
		// elevatorFloor: floor on which this elevator is found
		// elevatorPos: position of the elevator on its floor
		var elevatorFloor, elevatorPos int
		fmt.Scan(&elevatorFloor, &elevatorPos)
		elevators[elevatorFloor] = elevatorPos
	}

	oneTurn := false
	turn := 0
	for {
		// cloneFloor: floor of the leading clone
		// clonePos: position of the leading clone on its floor
		// direction: direction of the leading clone: LEFT or RIGHT
		var cloneFloor, clonePos int
		var direction string
		fmt.Scan(&cloneFloor, &clonePos, &direction)

		if cloneFloor == -1 {
			fmt.Println("WAIT")
			continue
		}

		var pos int
		if cloneFloor == exitFloor {
			pos = exitPos
		} else {
			pos = elevators[cloneFloor]
		}

		dir := direction == "RIGHT"
		if dir == (clonePos < pos) {
			fmt.Println("WAIT")
			oneTurn = false
		} else if oneTurn {
			fmt.Println("BLOCK")
			oneTurn = false
		} else {
			oneTurn = true
			fmt.Println("WAIT")
		}
	}
	turn++
}