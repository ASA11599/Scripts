import random

def keep_border_islands(matrix: list[list[int]]) -> list[list[int]]:
    def get_neighbors(pos: tuple[int, int]) -> list[tuple[int, int]]:
        neighbors: list[tuple[int, int]] = []
        if pos[0] != 0:
            neighbors.append((pos[0] - 1, pos[1]))
        if pos[0] != (len(matrix) - 1):
            neighbors.append((pos[0] + 1, pos[1]))
        if pos[1] != 0:
            neighbors.append((pos[0], pos[1] - 1))
        if pos[1] != (len(matrix[pos[0]]) - 1):
            neighbors.append((pos[0], pos[1] + 1))
        return neighbors
    result: list[list[int]] = [[0 for i in row] for row in matrix]
    visited: list[list[bool]] = [[False for i in row] for row in matrix]
    for ri in range(len(matrix)):
        for ci in range(len(matrix[ri])):
            on_border: bool = (ri == 0 or ri == (len(matrix) - 1)) or (ci == 0 or ci == (len(matrix[ri]) - 1))
            if on_border and matrix[ri][ci] == 1:
                visited[ri][ci] = True
                result[ri][ci] = 1
                queue: list[tuple[int, int]] = get_neighbors((ri, ci))
                while len(queue) > 0:
                    current: tuple[int, int] = queue.pop(0)
                    if (matrix[current[0]][current[1]] == 1) and not visited[current[0]][current[1]]:
                        visited[current[0]][current[1]] = True
                        result[current[0]][current[1]] = 1
                        queue += [n for n in get_neighbors(current) if (matrix[n[0]][n[1]])]
    return result

if __name__ == "__main__":
    m: list[list[int]] = [[random.choice([0, 1]) for j in range(5)] for i in range(5)]
    for r in m:
        print(r)
    print()
    for r in keep_border_islands(m):
        print(r)
