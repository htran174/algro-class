import heapq 

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

#input from user
n = int(input("Enter number of vertices: "))
graph = [[] for _ in range(n)]
e = int(input("Enter number of edges: "))

for _ in range(e):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())
    graph[u].append((v,w))
    graph[v].append((u,w))

src = int(input("Enter the source vertex: "))
result = dijkstra(graph, src)
print("Shortest distance from source: ", result)