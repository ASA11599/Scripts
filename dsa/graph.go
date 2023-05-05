package main
import "fmt"

type Graph struct {
    vertices map[int][]int
}

func NewGraph() *Graph {
    return &Graph{ vertices: make(map[int][]int) }
}

func (g *Graph) ContainsVertex(v int) bool {
    _, ok := g.vertices[v]
    return ok
}

func (g *Graph) AddVertex(v int) {
    if !g.ContainsVertex(v) {
        g.vertices[v] = make([]int, 0)
    }
}

func (g *Graph) AddEdge(src, dst int) {
    g.AddVertex(src)
    g.AddVertex(dst)
    g.vertices[src] = append(g.vertices[src], dst)
}

func (g *Graph) BFS(start int, visit func(int)) {
    visited := make(map[int]bool)
    q := []int{ start }
    for len(q) > 0 {
        current := q[0]
        q = q[1:]
        for _, n := range g.vertices[current] {
            if !visited[n] {
                q = append(q, n)
            }
        }
        visit(current)
        visited[current] = true
    }
}

func (g *Graph) DFS(start int, visit func(int)) {
    visited := make(map[int]bool)
    s := []int{ start }
    for len(s) > 0 {
        current := s[len(s) - 1]
        s = s[:len(s) - 1]
        for _, n := range g.vertices[current] {
            if !visited[n] {
                s = append(s, n)
            }
        }
        visit(current)
        visited[current] = true
    }
}

func main() {
    g := NewGraph()
    g.AddEdge(0, 9)
    g.AddEdge(9, 8)
    g.AddEdge(8, 0)
    fmt.Println(g)
    g.DFS(0, func(v int) { fmt.Println(v) })
}
