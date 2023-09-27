class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
   def __init__(self):
      self.headval = None

   def printList(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
         
   def insertAtBeginning(self,node):
      new_node = Node(node)
      new_node.nextval = self.headval
      self.headval = new_node
      
   def insertAtLast(self,node):
      if self.headval == None:
        self.headval = Node(node)
        return
      else:
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = Node(node)
        
   def insertAtMiddle(self,middleNode,node):
      if middleNode is None:
        print("The mentioned node is absent")
        return
      new_node = Node(node)
      new_node.nextval = middleNode.nextval
      middleNode.nextval = new_node
      
   # Function to remove a node from a linked list
   def removeNode(self, Removekey):
        # Start with the head of the linked list
      HeadVal = self.headval

        # Check if the linked list is not empty
      if (HeadVal is not None):
            # Check if the node to be removed is the head node
        if (HeadVal.dataval == Removekey):
            # Update the head to the next node (removing the current head)
            self.headval = HeadVal.nextval
            # Set the old head to None to free the memory
            HeadVal = None
            return

    # Traverse the linked list to find the node to remove
      while (HeadVal is not None):
        # Check if the current node's data matches the key to remove
        if HeadVal.dataval == Removekey:
            break
        # Keep track of the previous node
        prev = HeadVal
        # Move to the next node
        HeadVal = HeadVal.nextval

        # If the node to remove was not found in the linked list
      if (HeadVal is None):
        return

        # Update the previous node's "next" pointer to skip the node to remove
      prev.nextval = HeadVal.nextval
        # Set the node to remove to None to free the memory
      HeadVal = None

      
      
        
            
list = LinkedList()
list.headval = Node("Monday")
d1 = Node("Tuesday")
d2 = Node("Wednesday")
list.headval.nextval = d1
d1.nextval = d2
list.printList()
print("\n")
list.insertAtBeginning("Sunday")
list.printList()
print("\n")
list.insertAtLast("Thursday")
list.printList()
print("\n")
list.insertAtMiddle(list.headval.nextval,"Fri")

list.printList()
print("\n")

       
print("============Refreshing Linked list with fresh entries====================")

llist = LinkedList()
llist.insertAtBeginning("Mon")
llist.insertAtBeginning("Tue")
llist.insertAtBeginning("Wed")
llist.insertAtBeginning("Thu")
llist.printList()
print("\n")
llist.removeNode("Thu")
llist.printList()

"""A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer. Python does not have linked lists in its standard library. We implement the concept of linked lists using the concept of nodes as discussed in the previous chapter.

We have already seen how we create a node class and how to traverse the elements of a node.In this chapter we are going to study the types of linked lists known as singly linked lists. In this type of data structure there is only one link between any two data elements. We create such a list and create additional methods to insert, update and remove elements from the list.

Advantages Of Linked List:
Dynamic data structure: A linked list is a dynamic arrangement so it can grow and shrink at runtime by allocating and deallocating memory. So there is no need to give the initial size of the linked list.
No memory wastage: In the Linked list, efficient memory utilization can be achieved since the size of the linked list increase or decrease at run time so there is no memory wastage and there is no need to pre-allocate the memory.
Implementation: Linear data structures like stacks and queues are often easily implemented using a linked list.
Insertion and Deletion Operations: Insertion and deletion operations are quite easier in the linked list. There is no need to shift elements after the insertion or deletion of an element only the address present in the next pointer needs to be updated. 
Flexible: This is because the elements in Linked List  are not stored in contiguous memory locations unlike the array.
Efficient for large data: When working with large datasets linked lists play a crucial role as it can grow and shrink dynamically.
Scalability: Contains the ability to add or remove elements at any position.
Disadvantages Of Linked List:
Memory usage: More memory is required in the linked list as compared to an array. Because in a linked list, a pointer is also required to store the address of the next element and it requires extra memory for itself.
Traversal: In a Linked list traversal is more time-consuming as compared to an array. Direct access to an element is not possible in a linked list as in an array by index. For example, for accessing a node at position n, one has to traverse all the nodes before it.
Reverse Traversing: In a singly linked list reverse traversing is not possible, but in the case of a doubly-linked list, it can be possible as it contains a pointer to the previously connected nodes with each node. For performing this extra memory is required for the back pointer hence, there is a wastage of memory.
Random Access: Random access is not possible in a linked list due to its dynamic memory allocation.
Lower efficiency at times: For certain operations, such as searching for an element or iterating through the list, can be slower in a linked list.
Complex implementation:  The linked list implementation is more complex when compared to array. It requires a complex programming understanding.
Difficult to share data: This is because it is not possible to directly access the memory address of an element in a linked list.
Not suited for small dataset: Cannot provide any significant benefits on small dataset compare to that of an array.


Reference : https://www.geeksforgeeks.org/advantages-and-disadvantages-of-linked-list/
"""