#goal is to find reachable cities form source node
#BFS

from collections import deque
import march22_classwork1

def bfs(graph, start):
    visted = set() #set to tacked visted cities
    queue = deque([start])

    print("\nBFS Traversal Order:")
    while queue:
        city =  queue.popleft() #dequeue a city
        if city not in visted:
            print(city, end=" ") #printing visted city
            visted.add(city) #marking as visted city
            for neighbor in graph.get(city, []):
                if neighbor not in visted:
                    queue.append(neighbor)
                
if __name__ == "__main__":
    g = march22_classwork1.Graph()
    print("Enter number of Connection: ")
    edges = int(input())

    print("Now enter each connection in format: City1 City2")
    for _ in range(edges):
        u, v = input().split()
        g.add_edge(u, v)

    print("Enter starting City for BFS: ")
    start_city = input()
    bfs(g.graph,start_city)