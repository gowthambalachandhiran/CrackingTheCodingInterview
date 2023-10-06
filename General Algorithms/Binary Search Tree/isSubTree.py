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
        element.append(self.node)

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

## Build two trees a main tree names M and subtree named S
M = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
S = build_tree([20,18,23])

print(M.preOrderTraversal())
print(S.preOrderTraversal())

def is_sub_tree(preOrderListM,preOrderListS):
    if sorted(set(preOrderListM) & set(preOrderListS), key = preOrderListM.index) == preOrderListS:
        return True
    else:
        return False
        
print(is_sub_tree(M.preOrderTraversal(),S.preOrderTraversal()))