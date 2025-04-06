from typing import List

def is_valid(vertex: int, color: int, graph: List[List[int]], colors: List[int]) -> bool:
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True

def solve(vertex: int, graph: List[List[int]], k: int, colors: List[int]) -> bool:
    if vertex == len(graph):
        return True

    for color in range(1, k + 1):
        if is_valid(vertex, color, graph, colors):
            colors[vertex] = color
            if solve(vertex + 1, graph, k, colors):
                return True
            colors[vertex] = 0 

    return False

def graph_coloring(n: int, m: int, k: int, edges: List[List[int]]):
    graph = [[0] * n for _ in range(n)]
    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1  

    colors = [0] * n

    if solve(0, graph, k, colors):
        print(f"Coloring Possible with {k} Colors")
        print(f"Color Assignment: {colors}")
    else:
        print(f"Coloring Not Possible with {k} Colors")



if __name__ == "__main__":
    n1, m1, k1 = 4, 5, 3
    edges1 = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3]]
    graph_coloring(n1, m1, k1, edges1)

    print()

    n2, m2, k2 = 4, 5, 2
    edges2 = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3]]
    graph_coloring(n2, m2, k2, edges2)
