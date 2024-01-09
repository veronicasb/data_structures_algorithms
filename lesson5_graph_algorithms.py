
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

class Graph:
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
    
graph2 = Graph(num_nodes, edges)
# print(graph2)

graph2.add_edge((5, 6))
# print(graph2)

graph2.remove_edge((5, 6))
print(graph2)


# Adjacency Matrix - another more efficient way of representing graphs

"""
1. initiate a matrix of 0s the size of n * n where n is our number of nodes
2. for each node, fill the matrix with 1s depending on where each node has an edge

"""

# CHALLENGE: Create a class that creates an adjacency matrix

class Graph2:
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

# graph3 = Graph2(num_nodes, edges)
# print(graph3)


# GRAPH TRAVERSALS

# Breadth-First Search

