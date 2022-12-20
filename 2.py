paths_dfs = []
def dfs(graph, start, end, path=[]):

    global paths_dfs
    path = path + [start]
    if start == end:
        paths_dfs.append(path)
    for node in graph[start]:
        if node not in path:
            dfs(graph, node, end, path)

def bfs(graph, start, end):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        if vertex == end:
            yield path
        for current_vertex in graph[vertex]:
            if current_vertex not in path:
                queue.append(path + [current_vertex])

graph = {1: [2, 4], 2: [1, 5, 6], 3: [7, 8], 4: [1, 9, 10], 5: [2, 11, 12], 6: [2, 13, 14], 7: [3, 15, 16], 8: [3, 14, 1], 9: [4, 11, 12], 10: [4, 16], 11: [5, 9, 1], 12: [5, 9], 13: [6], 14: [6, 8], 15: [7], 16: [7, 10]}

print("graph = ", graph)
dfs(graph, 13, 15)
print("Поиск в глубину")
for path in paths_dfs:
    print(path)
print("=====================================")

path_bfs = bfs(graph, 13, 15)
print("Поиск в ширину")
for path in path_bfs:
    print(path)