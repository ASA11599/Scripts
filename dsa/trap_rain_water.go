package main

import "fmt"

func trapRainWater(height []int) int {
	// Result
	var waterUnits int = 0
	for {
		fmt.Println(height)
		// find the first and last non-zero heights
		foundFirstBar := false
		foundLastBar := false
		firstBarIdx := 0
		lastBarIdx := len(height) - 1
		for i := range height {
			if (!foundFirstBar) && (height[i] > 0) {
				firstBarIdx = i
				foundFirstBar = true
			}
			if height[i] > 0 {
				lastBarIdx = i
				foundLastBar = true
			}
		}
		// If the current level is flat, no water gets trapped here or above
		if (!foundFirstBar) || (!foundLastBar) {
			break
		}
		// If the current level has no empty space for water, no more water here or above
		if (lastBarIdx - firstBarIdx) <= 1 {
			break
		}
		// Count the water units at the current level (floor)
		for i := firstBarIdx; i <= lastBarIdx; i++ {
			// Water can only fill the spaces with no bar (0s)
			if height[i] == 0 {
				waterUnits++
			}
		}
		// Decrement each bar height to count water at the next level
		for i := range height {
			if height[i] > 0 {
				height[i]--
			}
		}
	}
	return waterUnits
}

func main() {
	fmt.Println(trapRainWater([]int{4, 2, 0, 3, 2, 5}))
}
