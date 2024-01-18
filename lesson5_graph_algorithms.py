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
print(graph2)

graph2.add_edge((5, 6))
print(graph2)

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

# Breadth-First Search (BFS) - search algorithm that visits all nodes at each level

"""
PSEUDOCODE

Main tool: queue - a data structure (list) that follows a FIFO (First In First Out) policy

1. BFS(G, root) where G is a graph and root is the root node of that graph
2.      create a queue called Q
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

    while root < len(discovered):
        
        # If a node is not yet discovered, mark it as discovered and create a queue for itself and its edge nodes
        if not discovered[root]:
            queue = [root]
            discovered[root] = True

            idx = 0

            while idx < len(queue):
                # dequeue
                current = queue[idx]
                idx += 1

                # check all edges of current node
                for node in graph.data[current]:
                    if not discovered[node]:
                        discovered[node] = True
                        queue.append(node)

            components.append(queue)
        root += 1

    connected = False if len(components) > 1 else True

    return f"All Connected: {connected} \nNumber of Components: {len(components)} \nConnected Components: {components}"

print(connected(graph4))


# Depth-First Search (DFS) - search algorithm that visits each node in a path down to its leaf

"""
PSEUDOCODE - iterative

Main tool: stack - a data structure that follows a LIFO (Last In First Out) policy

1. dfs_iterative(G, v) where G is a graph and v is a node
2.      let S be a stack
3.      S.push(v)
4.      while S is not empty:
5.          v = S.pop()
6.          if v is not labeled as discovered:
7.              label v as discovered
8.              for all edges from v to w in G.adjacentEdges(v):
9.                  S.push(w)

"""

def dfs_iterative(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    # everytime we pop something, we add to result list
    result = []

    stack.append(root)
    # dont mark root node as discovered just yet

    while len(stack) > 0:
        current = stack.pop()
        
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            # this for loop will iterate over all the nodes connected to the nodes under our current node
            for node in graph.data[current]:
                stack.append(node)

    return f"DFS of {root}: {result}"

print(dfs_iterative(graph2, 3))

"""
CHALLENGE: Recreate the DFS function recursively.

"""

"""
CHALLENGE: Determine shortest distance from one node to another using DFS.

"""

"""
CHALLENGE: Write a function to detect a cycle and number of cycles in a graph.

A cycle is a path that leads from a node back to itself. You can tell you have a cycle if you end up 
visiting a node that has already been discovered. 

"""


# Weighted Graphs - graph with weights associated with edges

num_nodes3 = 9
# 3rd element in each set represents the weight of the edge
edges3 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]


# Directed Graphs - graph with directions associates with edges

num_nodes4 = 5
# when creating adjacency lists, nodes will not point to each other like we saw in the first example
edges4 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
directed4 = True

# Write a class to represent weighted and directed graphs

class GraphWeightDirect:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.edges = edges
        self.directed = directed
        self.weighted = weighted

        # create an empty adjacency list
        self.data = [[] for _ in range(self.num_nodes)]

        # create an empty list that will store the weights corresponding to the nodes in the adjacency list
        self.weight = [[] for _ in range(self.num_nodes)]

        for edge in self.edges:
            if self.weighted:
                n1, n2, weight = edge
                self.data[n1].append(n2)
                self.weight[n1].append(weight)
                if not self.directed:
                    self.data[n2].append(n1)
                    self.weight[n2].append(weight)
            else:
                n1, n2 = edge
                self.data[n1].append(n2)
                if not self.directed:
                    self.data[n2].append(n1)

    def __repr__(self):
        status = "UNDIRECTED, "
        status = "DIRECTED, " if self.directed else status
            
        if self.weighted:
            status += "WEIGHTED"
            # zip allows you to aggregate elements from multiple iterables; returns an iterator containing tuples of corresponding elements
            return f"{status}\n" + "\n".join((f"{x}: {list(zip(y, z))}") for x, (y, z) in enumerate(zip(self.data, self.weight)))
        else:
            status += "UNWEIGHTED"
            return f"{status}\n" + "\n".join((f"{x}: {y}") for x, y in enumerate(self.data))
    
    def __str__(self):
        return self.__repr__()

weighted_graph1 = GraphWeightDirect(num_nodes3, edges3, weighted=True)
print(weighted_graph1)

directed_graph1 = GraphWeightDirect(num_nodes4, edges4, directed=True)
print(directed_graph1)
                

# Shortest Path

"""
Understanding whether a graph is weighted or unweighted is key in choosing the best approach. The Shortest Path approach 
can be performed on directed or undirected graphs.

The "shortest path" of a graph with NO weights (AKA path with the lowest number of nodes) can be found using BFS. 
Otherwise, if your graph has weights (doesn't matter if it's a directed or undirected graph), 
then DIJKSTRA'S ALGORITHM is your best bet. 

DIJKSTRA'S ALGORITHM (FOR UNDIRECTED GRAPHS)- find the shortest path (in terms of weight, not number of nodes) in a graph

1.Mark all nodes as unvisited. Create a set of unvisited nodes. 

2. Assign to all nodes a tentative distance value: set it to 0 for our initial node and infinity for all other nodes.
Set initial node as current.

3. For the current node, consider all of its unvisited neighbors and calculate their tentative distance through the current node. 
Compare newly calculated tentative distance to the current assigned value and assign the smaller one. 

4. When we are done considering all of the unvisited neighbors of the current node and calculating distances, mark the 
current node as visited and remove it from the unvisited set. A visited node should not be checked again.

5. If the destination node has been marked visited while planning a route between two specific nodes or if the smallest 
tentative distance among the nodes in the unvisited set is infinity while planning a complete travesal (this occurs when 
there is no connected between the initial node and remaining unvisited nodes), then stop. The algorithm is complete.

6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node, 
then go back to step 3.

"""

def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)

    # this variable allows us to track the path of the shortest path
    parent = [None] * len(graph.data)

    distance = [float('inf')] * len(graph.data)
    queue = []

    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1

        # update distances of all neighbors
        update_distances(graph, current, distance, parent)

        # find first unvisited node with the smallest distance/weight
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)   

        visited[current] = True

    # CHALLENGE: display the actual path of nodes taken to get to target
    path_nodes = [target]
    idx2 = target
    while parent[idx2]:
        path_nodes.append(parent[idx2])
        idx2 = parent[idx2]
    
    actual_path = " -> ".join(str(node) for node in path_nodes[::-1])

    return distance[target], actual_path


def update_distances(graph, current, distance, parent=None):
    # Update the distance of the current node's neighbors
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current 


def pick_next_node(distance, visited):
    # Pick the next unvisited node at the smallest distance
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node


num_nodes5 = 6
edges5 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (3, 5, 11), (4, 3, 4)]

graph5 = GraphWeightDirect(num_nodes5, edges5, weighted=True, directed=True)
print(graph5)

print(f'Shortest Path: {shortest_path(graph5, 0, 5)}')

graph6 = GraphWeightDirect(num_nodes3, edges3, weighted=True)
print(graph6)

print(f'Shortest Path: {shortest_path(graph6, 0, 7)}')

print(f'Shortest Path: {shortest_path(graph6, 2, 8)}')