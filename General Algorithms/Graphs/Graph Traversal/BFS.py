# Create a graph given in the above diagram.
graph_elements = {
   "a": ["b", "c"],
   "b": ["a", "d"],
   "c": ["a", "d"],
   "d": ["e"],
   "e": ["d"]
}

# to print a BFS of a graph
def bfs(node):

    # mark vertices as False means not visited
    visited = [False] * (len(graph_elements))

    # make an empty queue for bfs
    queue = []

    # mark gave node as visited and add it to the queue
    visited.append(node)
    queue.append(node)

    while queue:
        # Remove the front vertex or the vertex at the 0th index from the queue and print that vertex.
        v = queue.pop(0)
        print(v, end=" ")

        # Get all adjacent nodes of the removed node v from the graph hash table.
        # If an adjacent node has not been visited yet,
        # then mark it as visited and add it to the queue.
        for neigh in graph_elements[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)


# Driver Code
if __name__ == "__main__":
    bfs('b')

"""Time Complexity Analysis:

In the worst case, each node and edge will be visited once. So, the time complexity of this BFS algorithm is O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.
In this specific example, the graph has 5 vertices and 4 edges, so the time complexity is O(5 + 4), which simplifies to O(9), i.e., O(V + E).
Space Complexity Analysis:

The space complexity is determined by the space used for the visited list and the queue. Both have a space complexity of O(V), where V is the number of vertices in the graph, as they store information for each vertex.
Overall, this code performs a breadth-first traversal of the graph starting from node 'b' and prints the visited nodes in BFS order.




"""