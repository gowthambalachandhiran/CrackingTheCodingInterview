# Define the graph as an adjacency list where each node maps to its neighbors.
graph_elements = {
   "a": ["b", "c"],
   "b": ["a", "d"],
   "c": ["a", "d"],
   "d": ["e"],
   "e": ["d"]
}

# Define a DFS (Depth-First Search) function using a stack.
def dfs(graph, starting_node):
    visited = []  # To keep track of visited nodes
    stack = []    # Stack to perform DFS

    stack.append(starting_node)  # Initialize the stack with the starting node

    while stack:
        current_node = stack.pop()  # Pop the last node from the stack (LIFO)

        if current_node not in visited:
            print(current_node, "->\t")  # Print the current node and "->"
            visited.append(current_node)  # Mark the current node as visited

        # Push unvisited neighbors onto the stack in reverse order to maintain DFS order
        for neighbor in reversed(graph[current_node]):
            if neighbor not in visited:
                stack.append(neighbor)

# Call the DFS function with the graph and starting node "b"
dfs(graph_elements, "b")



"""Time Complexity Analysis:

In the worst case, each node and edge will be visited once. So, the time complexity of this DFS algorithm is O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.
In this specific example, the graph has 5 vertices and 4 edges, so the time complexity is O(5 + 4), which simplifies to O(9), i.e., O(V + E).
This code will start the DFS from the node "b" and print the visited nodes in a depth-first traversal order, as well as the "->" symbol to indicate the direction of traversal. It helps you understand how the DFS algorithm explores the graph starting from a given node."""