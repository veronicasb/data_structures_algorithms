
# simple representation of a graph

num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (2, 3), (3, 1), (1, 4), (3, 4)]
print(num_nodes, len(edges))


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

        # set our number of nodes accordingly
        nodes = set()
        for element in self.edges:
            for node in element:
                nodes.add(node)
        self.num_nodes = len(nodes)
        
        # Create a new empty data list with the right number of empty lists
        self.data = [[] for _ in range(self.num_nodes)]
        # Insert into proper lists
        for n1, n2 in self.edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        
    def remove_edge(self, edge):
        # remove edge from our existing list
        self.edges.remove(edge)

        # set our number of nodes accordingly
        nodes = set()
        for element in self.edges:
            for node in element:
                nodes.add(node)
        self.num_nodes = len(nodes)

        # Create a new empty data list with the right number of empty lists
        self.data = [[] for _ in range(self.num_nodes)]
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
# print(graph2)

