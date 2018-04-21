package main

import "fmt"

//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func dist(exitFloor, exitPos int, elevators [][]int) int {
	return 0
}

func choose_elevator(nbAdditionalElevators, nbElevators, exitFloor, exitPos int, elevators [][]int) {
	nbFloors := len(elevators)
	/**
	 * For every floor, I try to minimize the length
	 * between current position and next one of next floor elevator
	 * If result not good, I try to replace next floor elevator with a new one
	 * If still not enough, either second-next floor should be replaced or both
	 * This is an iterative process up to the top of the map
	 **/
}

func main() {
	// nbFloors: number of floors
	// width: width of the area
	// nbRounds: maximum number of rounds
	// exitFloor: floor on which the exit is found
	// exitPos: position of the exit on its floor
	// nbTotalClones: number of generated clones
	// nbAdditionalElevators: number of elevators which can be build
	// nbElevators: number of elevators
	var nbFloors, width, nbRounds, exitFloor, exitPos, nbTotalClones, nbAdditionalElevators, nbElevators int
	fmt.Scan(&nbFloors, &width, &nbRounds, &exitFloor, &exitPos, &nbTotalClones, &nbAdditionalElevators, &nbElevators)

	elevators := make([][]int, nbFloors)
	for i := 0; i < nbElevators; i++ {
		// elevatorFloor: floor on which this elevator is found
		// elevatorPos: position of the elevator on its floor
		var elevatorFloor, elevatorPos int
		fmt.Scan(&elevatorFloor, &elevatorPos)
		if elevators[elevatorFloor] == nil {
			elevators[elevatorFloor] = make([]int, 0)
		}
		elevators[elevatorFloor] = append(elevators[elevatorFloor], elevatorPos)
	}

	// Find where to put elevatorPos

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
			pos = elevators[cloneFloor][0]
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
