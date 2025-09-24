import heapq

def prim(graph, n):
    visited = [False] * n
    min_heap = [(0,0)]
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))

    return total_cost

#user inoput
n = int(input("Enter number of vertices: "))
graph = [[] for _ in range(n)]
e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())
    graph[u].append((v,w))
    graph[v].append((u,w))

print("Minimun cost to connect all nodes: ", prim(graph, n))