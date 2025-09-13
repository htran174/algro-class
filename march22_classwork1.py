#define class
#undirected graph algro

class Graph:
    def __init__(self):
        #Dictionary
        self.graph= {}
        
    def add_edge(self, u, v):
        #if u is not key, then initialize its list
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        #add connection (undirected graph)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        #print all note and their connection
        print("\nGraph Representation (Adjacency List)")
        for city in self.graph:
            print(f"{city} ----> {self.graph[city]}")
    
#Main
if __name__ == "__main__":
    g = Graph()
    edges = int(input("Enter the number of connection (edges): "))

    print("Now enter each connection in format: City1 City2")
    for _ in range(edges):
        u, v = input().split()
        g.add_edge(u, v)
        
    g.display()