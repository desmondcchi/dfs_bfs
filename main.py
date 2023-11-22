from collections import deque
from typing import List


def bfs(s: int, adj_matrix: List[List[int]]) -> None:
    res = ""
    visited = [False] * len(adj_matrix)
    queue = deque()

    queue.append(s)
    visited[s] = True

    while queue:
        curr = queue.popleft()
        res += str(curr) + " "

        for i, n in enumerate(adj_matrix[curr]):
            if n == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

    print("BFS: " + res)


def dfs(s: int, adj_matrix: List[List[int]]) -> None:
    res = ""
    pre = ""
    post = ""
    visited = [False] * len(adj_matrix)
    stack = []

    stack.append(s)

    while stack:
        curr = stack.pop()

        if not visited[curr]:
            res += str(curr) + " "
            visited[curr] = True

        for i, n in reversed(list(enumerate(adj_matrix[curr]))):
            if n == 1 and not visited[i]:
                stack.append(i)

    print("DFS: " + res)


time = 1
def dfs_prepost(
    v: int,
    pre: List[int],
    post: List[int],
    visited: List[bool],
    adj_matrix: List[List[int]],
) -> (List[int], List[int]):
    """
    Returns list of preorder and postorder visit times (times correspond with the index)
    """
    global time

    pre[v] = time
    time += 1
    visited[v] = True

    for i, n in list(enumerate(adj_matrix[v])):
        if n == 1 and not visited[i]:
            dfs_prepost(i, pre, post, visited, adj_matrix)

    post[v] = time
    time += 1

    #A  B  C  D  E  F  G  H  I
adj_matrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0],  # A = 0
    [0, 0, 1, 0, 0, 0, 0, 0, 0],  # B = 1
    [0, 0, 0, 1, 1, 0, 0, 0, 0],  # C = 2
    [0, 0, 0, 0, 1, 0, 1, 0, 0],  # D = 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # E = 4
    [0, 0, 0, 0, 1, 0, 0, 0, 0],  # F = 5
    [0, 0, 0, 0, 0, 1, 0, 0, 1],  # G = 6
    [0, 0, 0, 1, 0, 0, 1, 0, 0],  # H = 7
    [0, 0, 0, 0, 0, 1, 0, 0, 0],  # I = 8
]

bfs(0, adj_matrix)
dfs(0, adj_matrix)

pre = [0] * len(adj_matrix)
post = [0] * len(adj_matrix)
visited = [False] * len(adj_matrix)
dfs_prepost(0, pre, post, visited, adj_matrix)
time = 1
print(pre)
print(post)
