from collections import deque
from typing import List

def bfs(v: int, adj_matrix: List[List[int]]) -> None:
    res = ""
    visited = [False] * len(adj_matrix)
    queue = deque()

    queue.append(v)
    visited[v] = True

    while queue:
        curr = queue.popleft()
        res += str(curr) + " "

        for i, n in enumerate(adj_matrix[curr]):
            if n == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

    print("BFS: " + res)


def dfs(v: int, adj_matrix: List[List[int]]) -> None:
    res = ""
    visited = [False] * len(adj_matrix)
    stack = []

    stack.append(v)

    while stack:
        curr = stack.pop()

        if not visited[curr]:
            res += str(curr) + " "
            visited[curr] = True
        
        for i, n in enumerate(adj_matrix[curr]):
            if n == 1 and not visited[i]:
                stack.append(i)

    print("DFS: " + res)

adj_matrix = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0],  # A = 0
    [1, 0, 1, 0, 1, 0, 1, 0, 0],  # B = 1
    [1, 1, 0, 1, 0, 0, 0, 0, 1],  # C = 2
    [1, 0, 1, 0, 0, 0, 0, 0, 0],  # D = 3
    [0, 1, 0, 0, 0, 0, 0, 1, 1],  # E = 4
    [0, 0, 0, 0, 0, 0, 1, 1, 0],  # F = 5
    [0, 1, 0, 0, 0, 1, 0, 1, 0],  # G = 6
    [0, 0, 0, 0, 1, 1, 1, 0, 1],  # H = 7
    [0, 0, 1, 0, 1, 0, 0, 1, 0],  # I = 8
]

bfs(0, adj_matrix)
dfs(0, adj_matrix)
