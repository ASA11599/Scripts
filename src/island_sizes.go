package main

import "fmt"

func getIslandSizes(matrix [][]int) []int {
	sizes := make([]int, 0)
	visited := make([][]bool, len(matrix))
	for row := range visited {
		visited[row] = make([]bool, len(matrix[row]))
	}
	getNeighbors := func(row int, col int) [][]int {
		neighbors := make([][]int, 0, 4)
		if row > 0 {
			neighbors = append(neighbors, []int{row - 1, col})
		}
		if row < (len(matrix) - 1) {
			neighbors = append(neighbors, []int{row + 1, col})
		}
		if col > 0 {
			neighbors = append(neighbors, []int{row, col - 1})
		}
		if col < (len(matrix[row]) - 1) {
			neighbors = append(neighbors, []int{row, col + 1})
		}
		return neighbors
	}
	var visit func(int, int) int
	visit = func(row int, col int) int {
		if !visited[row][col] {
			visited[row][col] = true
			if matrix[row][col] == 1 {
				currentSize := 1
				for _, neighbor := range getNeighbors(row, col) {
					currentSize += visit(neighbor[0], neighbor[1])
				}
				return currentSize
			}
			return 0
		}
		return 0
	}
	for row := range matrix {
		for col := range matrix[row] {
			islandSize := visit(row, col)
			if islandSize > 0 {
				sizes = append(sizes, islandSize)
			}
		}
	}
	return sizes
}

func printMatrix(matrix [][]int) {
	for row := range matrix {
		fmt.Println(matrix[row])
	}
}

func main() {
	m := [][]int{[]int{1, 0, 0, 1, 1}, []int{1, 1, 0, 1, 0}, []int{0, 1, 0, 0, 1}, []int{0, 0, 1, 1, 0}, []int{1, 1, 0, 0, 0}}
	printMatrix(m)
	fmt.Println("Island sizes:", getIslandSizes(m))
}
