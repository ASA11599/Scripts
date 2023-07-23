import typing

class Graph(object):
    def __init__(self) -> None:
        self.__vs: set[str] = set()
        self.__es: dict[tuple[str, str], float] = {}
    def contains_vertex(self, value: str) -> bool:
        return value in self.__vs
    def contains_edge(self, src: str, dst: str) -> bool:
        return (src, dst) in self.__es
    def add_vertex(self, value: str) -> None:
        self.__vs.add(value)
    def add_edge(self, src: str, dst: str, w: float) -> None:
        self.__es[(src, dst)] = w
    def out_edges(self, vertex: str) -> list[tuple[tuple[str, str], float]]:
        out_edge_list: list[tuple[tuple[str, str], float]] = []
        for e in self.__es:
            if e[0] == vertex:
                out_edge_list.append((e, self.__es[e]))
        return out_edge_list


def convert_currency(facts: list[tuple[float, str, float, str]], src_value: float, src: str, dst: str) -> typing.Optional[float]:
    # Create a graph that will contain currencies as vertices and ratios as edges
    g: Graph = Graph()
    for fact in facts:
        g.add_vertex(fact[1])
        g.add_vertex(fact[3])
        g.add_edge(fact[1], fact[3], (fact[2] / fact[0]))
        g.add_edge(fact[3], fact[1], (fact[0] / fact[2]))
    # Create a queue to store (current_value, vertex)
    q: list[tuple[float, str]] = [(src_value, src)]
    # Keep track of the visited vertices
    visited: set[str] = set()
    while (len(q) > 0):
        current_vertex: tuple[float, str] = q.pop(0)
        visited.add(current_vertex[1])
        # If we are at the destination, return the current value
        if current_vertex[1] == dst:
            return current_vertex[0]
        # Still not at the destination, keep exploring neighbors
        for oe in g.out_edges(current_vertex[1]):
            if oe[0][1] not in visited:
                # Add this neighbor to the queue
                q.append((current_vertex[0] * oe[1], oe[0][1]))
    # Could not reach destination: impossible to convert
    return None


if __name__ == "__main__":
    print(convert_currency(
        facts=[
            (3, "EUR", 3.33, "USD"),
            (141.69, "JPY", 1, "USD"),
            (1, "USD", 0.87, "CHF"),
            (157.69, "JPY", 1, "EUR"),
            (2, "USD", 2.64, "CAD")
        ],
        src_value=5,
        src="CHF",
        dst="JPY"
    ))

