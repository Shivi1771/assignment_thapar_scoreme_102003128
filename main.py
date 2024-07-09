
### 2. `main.py`

"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    """
    Computes the longest path in a Directed Acyclic Graph (DAG).

    Parameters:
    - graph (list): A list of lists, where graph[i] contains tuples (j, w)
                    representing an edge from node i to node j with weight w.

    Returns:
    - int: The length of the longest path in the graph.
    """
    # Get topological order of the graph nodes
    topo_order = topological_sort(graph)
    # Calculate the longest path using the topological order
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    """
    Performs topological sorting on a DAG.

    Parameters:
    - graph (list): A list of lists, where graph[i] contains tuples (j, w)
                    representing an edge from node i to node j with weight w.

    Returns:
    - list: A list of nodes in topologically sorted order.
    """
    num_nodes = len(graph)
    order = []  # List to store the topological order
    visited = [False] * num_nodes  # List to keep track of visited nodes
    
    def depth_first_search(node):
        """
        Helper function to perform DFS and find the topological order.

        Parameters:
        - node (int): The current node being visited.
        """
        visited[node] = True  # Mark the current node as visited
        for neighbor, _ in graph[node]:  # Explore all neighbors of the current node
            if not visited[neighbor]:
                depth_first_search(neighbor)  # Recursively visit unvisited neighbors
        order.append(node)  # Append the current node to the order list after visiting all neighbors
    
    for node in range(num_nodes):
        if not visited[node]:  # Start DFS from unvisited nodes
            depth_first_search(node)
    
    order.reverse()  # Reverse the order list to get the topological order
    return order

def calculate_longest_path(graph, topo_order):
    """
    Calculates the longest path in a DAG given its topological order.

    Parameters:
    - graph (list): A list of lists, where graph[i] contains tuples (j, w)
                    representing an edge from node i to node j with weight w.
    - topo_order (list): A list of nodes in topologically sorted order.

    Returns:
    - int: The length of the longest path in the graph.
    """
    num_nodes = len(graph)
    max_dist = [-float('inf')] * num_nodes  # Initialize distances to negative infinity

    for node in topo_order:
        if max_dist[node] == -float('inf'):  # If node has not been visited, set its distance to 0
            max_dist[node] = 0
        for neighbor, weight in graph[node]:  # Explore all neighbors of the current node
            # Update the distance to the neighbor if a longer path is found
            if max_dist[node] + weight > max_dist[neighbor]:
                max_dist[neighbor] = max_dist[node] + weight
    
    return max(max_dist)  # Return the maximum distance found