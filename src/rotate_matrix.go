package main

import (
	"fmt"
)

func rotateMatrixOnce(matrix [][]int, direction int) [][]int {
	if direction == 0 {
		return matrix
	} else if (direction == -1) || (direction == 1) {
		nColumns := len(matrix[0])
		nRows := len(matrix)
		rotated := make([][]int, nColumns)
		for i := range rotated {
			rotated[i] = make([]int, nRows)
		}
		for row := range rotated {
			for col := range rotated[row] {
				if direction == 1 {
					rotated[row][col] = matrix[nRows-1-col][row]
				} else if direction == -1 {
					rotated[row][col] = matrix[col][nColumns-1-row]
				}
			}
		}
		return rotated
	} else {
		return matrix
	}
}

func rotateMatrix(matrix [][]int, rotation int) [][]int {
	rotated := matrix
	rotation = rotation % 4
	if rotation == 0 {
		return rotated
	} else {
		if rotation < 0 {
			for r := 0; r > rotation; r-- {
				rotated = rotateMatrixOnce(rotated, -1)
			}
		} else if rotation > 0 {
			for r := 0; r < rotation; r++ {
				rotated = rotateMatrixOnce(rotated, 1)
			}
		}
		return rotated
	}
}

func printMatrix(matrix [][]int) {
	for _, row := range matrix {
		fmt.Println(row)
	}
}

func main() {
	matrix := [][]int{[]int{1, 2, 3}, []int{4, 5, 6}, []int{7, 8, 9}}
	fmt.Println("matrix:")
	printMatrix(matrix)
	fmt.Println()
	rotations := []int{0, 1, -1, 2, -2, 3, -3, 4, -4}
	for i := range rotations {
		fmt.Println("rotated clockwise", rotations[i], "times:")
		printMatrix(rotateMatrix(matrix, rotations[i]))
		fmt.Println()
	}
}
