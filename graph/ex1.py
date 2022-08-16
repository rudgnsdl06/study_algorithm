# #ex1
# def facto(n):
#     num = 1
#     if n<1:
#         return 1
#     return n*facto(n-1)

# print(facto(5))

# #ex2
# graph = [
#     [0, 7, 5],
#     [7, 0, -1],
#     [5, -1, 0]
#     ]

# print(graph)

# graph = [[] for _ in range(3)]

# graph[0].append((1,7))
# graph[0].append((2,5))

# graph[1].append((0,7))

# graph[2].append((2,5))

# print(graph)

# #ex3- DFS
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if visited[i] == False:
#             dfs(graph, i, visited)

# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9

# dfs(graph, 1, visited)

# #ex4 - BFS

# from collections import deque
# def BFS(graph, start, visited):

#     queue = deque([start])
#     visited[start]=True

#     while queue:
#         print(queue)
#         v = queue.popleft()
#         print(v, end=' ')

#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9

# BFS(graph, 1, visited)

