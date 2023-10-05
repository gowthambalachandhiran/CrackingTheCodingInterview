class BinarySearchTree:
    def __init__(self, node):
        # Constructor for BinarySearchTree class, initializes a node with given value
        self.node = node
        self.left = None  # Initialize left child as None
        self.right = None  # Initialize right child as None

    def add_child(self, data):
        # Method to add a child node to the tree
        if data == self.node:
            return data  # If the data to be added is equal to the current node, return data
        if data < self.node:  # If data is less than the current node
            if self.left:  # If left child exists
                self.left.add_child(data)  # Recursively add data to the left subtree
            else:
                self.left = BinarySearchTree(data)  # Create a new left child with the data
        else:  # If data is greater than the current node
            if self.right:  # If right child exists
                self.right.add_child(data)  # Recursively add data to the right subtree
            else:
                self.right = BinarySearchTree(data)  # Create a new right child with the data

    def inOrderTraversal(self):
        # Method for in-order traversal of the tree, returns a list of elements
        element = []
        if self.left:
            element += self.left.inOrderTraversal()  # Recursively traverse left subtree
        element.append(self.node)  # Append current node
        if self.right:
            element += self.right.inOrderTraversal()  # Recursively traverse right subtree
        return element

    # Similar methods for pre-order and post-order traversal with the same logic

    def search(self, data):
        # Method to search for data in the tree
        if self.node == data:  # If current node's value matches the data
            return data
        if data < self.node:  # If data is less than the current node
            if self.left:  # If left child exists
                return self.left.search(data)  # Recursively search in the left subtree
            else:
                return False  # Data not found in the left subtree
        else:  # If data is greater than the current node
            if self.right:  # If right child exists
                return self.right.search(data)  # Recursively search in the right subtree
            else:
                return False  # Data not found in the right subtree

    def treeSum(self):
        # Method to calculate the sum of all elements in the tree
        sum = 0
        sum += self.node  # Add current node's value to sum
        sum += self.left.treeSum() if self.left else 0  # Add left subtree's sum if it exists, else add 0
        sum += self.right.treeSum() if self.right else 0  # Add right subtree's sum if it exists, else add 0
        return sum

    def findMin(self):
        # Method to find the minimum value in the tree
        if self.left:  # If left child exists
            return self.left.findMin()  # Recursively find minimum in the left subtree
        else:
            return self.node  # Return current node's value if no left child exists

    def findMax(self):
        # Method to find the maximum value in the tree
        if self.right:  # If right child exists
            return self.right.findMax()  # Recursively find maximum in the right subtree
        else:
            return self.node  # Return current node's value if no right child exists
            
    def preOrderTraversal(self):
        # Initialize an empty list to store the elements in pre-order
        element = []

        # Append the current node's value to the list (constant time - O(1))
        element += self.node

        # If the left child exists, recursively traverse the left subtree
        if self.left:
            element += self.left.preOrderTraversal()

        # If the right child exists, recursively traverse the right subtree
        if self.right:
            element += self.right.preOrderTraversal()

        # Return the list of elements in pre-order
        return element

    def postOrderTraversal(self):
        # Initialize an empty list to store the elements in post-order
        element = []

        # If the left child exists, recursively traverse the left subtree
        if self.left:
            element += self.left.postOrderTraversal()

        # If the right child exists, recursively traverse the right subtree
        if self.right:
            element += self.right.postOrderTraversal()

        # Append the current node's value to the list (constant time - O(1))
        element.append(self.node)

        # Return the list of elements in post-order
        return element



def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTree(elements[0])  # Create a root node with the first element

    for i in range(1, len(elements)):
        root.add_child(elements[i])  # Add the rest of the elements to the tree

    return root  # Return the root of the built tree


if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)  # Build a tree with country names

    print("UK is in the list? ", country_tree.search("UK"))  # Search for "UK"
    print("Sweden is in the list? ", country_tree.search("Sweden"))  # Search for "Sweden"

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])  # Build a tree with numbers
    print("In order traversal gives this sorted list:", numbers_tree.inOrderTraversal())  # Print in-order traversal
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])  # Build another tree with numbers
    print("In order traversal gives this sorted list:", numbers_tree.postOrderTraversal())  # Print post-order traversal
    print("sum of tree", numbers_tree.treeSum())  # Calculate and print the sum of tree
    print("Minimum=", numbers_tree.findMin())  # Find and print the minimum value in the tree
    print("Maximum=", numbers_tree.findMax())  # Find and print the maximum value in the tree

        
"""Time Complexity Analysis:

add_child: O(h) where 'h' is the height of the tree.
inOrderTraversal, preOrderTraversal, postOrderTraversal, search, treeSum, findMin, findMax: O(h) where 'h' is the height of the tree.
build_tree: O(n) for inserting 'n' elements into the tree, assuming the tree remains balanced.
Space Complexity:

The space complexity depends on the depth of the recursive calls, which can be at most 'h' in the worst case, where 'h' is the height of the tree. So, the space complexity of most methods is O(h).

In other words

In-order, Pre-order, and Post-order traversals are Depth-First traversals.

For a Graph, the complexity of a Depth First Traversal is O(n + m), where n is the number of nodes, and m is the number of edges.

Since a Binary Tree is also a Graph, the same applies here. The complexity of each of these Depth-first traversals is O(n+m).

Since the number of edges that can originate from a node is limited to 2 in the case of a Binary Tree, the maximum number of total edges in a Binary Tree is n-1, where n is the total number of nodes.

The complexity then becomes O(n + n-1), which is O(n).

For example

Algo -- <b>
    PreOrderTrav():-----------------T(n)<b>
    if root is null---------------O(1)<b>
      return null-----------------O(1)<b>
    else:-------------------------O(1)<b>
      print(root)-----------------O(1)<b>
      PreOrderTrav(root.left)-----T(n/2)<b>
      PreOrderTrav(root.right)----T(n/2)<b>

"""