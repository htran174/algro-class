# Define the DFS function using recursion 

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node)
        visited.add(node)
        
        for neighbour in graph.get(node, []):
            dfs(graph, neighbour, visited) #Recursive DFS call for the neighbor 

# Main block of code 
if __name__ == "__main__":
    graph = {}

    print("Enter the number of connections in the graph (edges):")
    edges = int(input())
    
    print("Now enter each connection in the format: node1 node2")
    print("This will assume the graph is undirected (2-way connections)")

    for _ in range(edges):
        u, v = input().split()

        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        
        if v not in graph:
            graph[v] = []
        graph[v].append(u)
    
    print("Enter the starting node for DFS traversal:")
    start_node = input()

    print("\nDFS Traversal Order:")
    dfs(graph, start_node)