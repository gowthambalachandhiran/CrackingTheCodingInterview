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