import sys
# input = sys.stdin.readline

k = int(input())

full_graph = []

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    full_graph.append(graph)

def dfs(graph, start, visit, colors):
    stack = [(start, 1)]
    
    while stack:
        node, color = stack.pop()

        if visit[node] == 0:
            visit[node] = 1
            colors[node] = color
            for value in graph[node]:
                stack.append((value, -color))
        elif colors[node] != color:
            return "NO"

    return "YES"

for graph in full_graph:
    v = len(graph) - 1
    visit = [0] * (v+1)
    colors = [0] * (v+1)

    result = "YES"
    for i in range(1, v+1):
        if visit[i] == 0:
            temp_result = dfs(graph, i, visit, colors)
            if temp_result == "NO":
                result = "NO"
                break

    print(result)