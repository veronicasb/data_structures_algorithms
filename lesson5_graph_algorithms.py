# BFS, DFS, and Shortest Path

# simple representation of a graph

num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (2, 3), (3, 1), (1, 4), (3, 4)]
# print(num_nodes, len(edges))


# Adjacency Lists - a more efficient way to represent graphs

# create a class to represent a graph as an adjacency list in Python

"""
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
    
        # when iterating over an object, if the iterating variable isnt being used, 
        # it's best to set it as _
    
        # create a list of empty lists where each empty list represents a node
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            # insert into proper lists
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    # Always make sure classes have a good string representation
    def __repr__(self):
        # enumerate function lists elements in an iterable object with its index as a tuple
        return "\n".join([ f"{n}: {neighbors}" for n , neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()
"""

# graph1 = Graph(num_nodes, edges)

# print(graph1)

# CHALLENGE: Write a function to add an edge to a graph represented as an adjacency list

# CHALLENGE: Write a function to remove an edge from a graph represented as an adjacency list

class GraphList:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = edges
        """
        when iterating over an object, if the iterating variable isnt being used, 
        it's best to set it as _
        """
        # create a list of empty lists where each empty list represents a node
        self.data = [[] for _ in range(self.num_nodes)]
        for n1, n2 in self.edges:
            # insert into proper lists
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def add_edge(self, edge):
        # add new edge to our edges list
        self.edges.append(edge)

        # get our new number of nodes
        nodes = set()
        [[nodes.add(node) for node in element] for element in self.edges]
        
        # Create a new empty data list with the right number of empty lists
        self.data = [[] for _ in range(len(nodes))]
        # Insert into proper lists
        for n1, n2 in self.edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        
    def remove_edge(self, edge):
        # remove edge from our existing list
        self.edges.remove(edge)

        # get our new number of nodes
        nodes = set()
        [[nodes.add(node) for node in element] for element in self.edges]

        # Create a new empty data list with the right number of empty lists
        self.data = [[] for _ in range(len(nodes))]
        # Insert into proper lists
        for n1, n2 in self.edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
            
    """
    Always make sure classes have a good string representation
    """
    def __repr__(self):
        # enumerate function lists elements in an iterable object with its index as a tuple
        return "\n".join([ f"{n}: {neighbors}" for n , neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()
    
graph2 = GraphList(num_nodes, edges)
# print(graph2)

graph2.add_edge((5, 6))
# print(graph2)

graph2.remove_edge((5, 6))
print(graph2)


# Adjacency Matrix - another more efficient way of representing graphs

"""
1. initiate a matrix of 0s the size of n * n where n is our number of nodes
2. fill the matrix with 1s depending on where each node has an edge

"""

# CHALLENGE: Create a class that creates an adjacency matrix

class GraphMatrix:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = edges
        # initialize matrix of 0s the size of n
        self.adjacency_matrix = [[0 for y in range(self.num_nodes)] for x in range(self.num_nodes)]

        # fill in matrix with 1s where edges exist
        for n1, n2 in self.edges:
            self.adjacency_matrix[n1][n2] = 1
            self.adjacency_matrix[n2][n1] = 1

    def __repr__(self):
        # enumerate function lists elements in an iterable object with its index as a tuple
        return "\n".join([f"{[y for y in x]}" for x in self.adjacency_matrix])

    def __str__(self):
        return self.__repr__()

graph3 = GraphMatrix(num_nodes, edges)
print(graph3)


# GRAPH TRAVERSALS

# Breadth-First Search (BFS)

"""
PSEUDOCODE

1. BFS(G, root) where G is a graph and root is the root node of that graph
2.      create a queue called Q - a queue is a data structure (list) that follows a FIFO (First In First Out) policy
3.      label root as it is discovered
4.      Q.enqueue(root) - enqueue is the acti of adding an element to a queue
5.      while Q is not empty:
6.          v = Q.dequeue() - dequeue is the act of removing an element from a queue
7.          if v is equal to the goal:
8.              return v
9.          otherwise, for all edges from v to w in G.adjacentEdges(v):
10.             if w is not labeled as discovered:
11.                 label w as discovered
12.                 Q.enqueue(w)

"""

def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)

    # we can track distance - this will show us the number of edges away from the our root node in list order
    distance = [None] * len(graph.data)

    # we can track parents - this will show us the parent of a node relative to our root node in list order
    parent = [None] * len(graph.data)

    discovered[root] = True
    queue.append(root)

    distance[root] = 0

    # Python doesnt support a dequeue operation by default, so we'll track indexes
    idx = 0

    while idx < len(queue):
        # dequeue
        current = queue[idx]
        idx += 1

        # check all edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                # tracking distance
                distance[node] = 1 + distance[current]
                
                # tracking parents
                parent[node] = current

                discovered[node] = True
                queue.append(node)

    return queue, distance, parent

# lets use graph2 for testing

print(bfs(graph2, 3))

"""
CHALLENGE: Write a function to check if all nodes are connected (using BFS). Also, check how many connected 
components exist and what they're connected to. Use the below example data.

1. Perform BFS starting with the first node - retrieve the connected components
2. Then, find the next node that is not yet visited and perform BFS on that
3. Repeat until all nodes are visited

"""

num_nodes2 = 9
edges2 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]
print(num_nodes2, len(edges2))

graph4 = GraphList(num_nodes2, edges2)
print(graph4)

"""
A function that checks if all nodes are connected, how many connected components exist, and what they're connected to.

Input:
1. graph - a GraphList object (an adjacency list)
2. root - an int representing a node in the adjacency list

Output:
1. connected - a Boolean that declares if all nodes in a graph are connected or not
2. components - an int representing the number of connected components
3. connections - a list of connected components

"""

def connected(graph, root=0):
    components = []
    discovered = [False] * len(graph.data)
    connected = False

    while root < len(discovered):
        
        if discovered[root] == False:
            queue = []
            
            discovered[root] = True
            queue.append(root)

            idx = 0

            while idx < len(queue):
                # dequeue
                current = queue[idx]
                idx += 1

                # check all edges of current
                for node in graph.data[current]:
                    if not discovered[node]:
                        discovered[node] = True
                        queue.append(node)

            components.append(queue)
        root += 1
    if len(components) == 1:
        connected = True

    return f"All Connected: {connected} \nNumber of Components: {len(components)} \nConnected Components: {components}"

print(connected(graph4))


# Depth-First Search (DFS)