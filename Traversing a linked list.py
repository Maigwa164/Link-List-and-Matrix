#definning a node
class Node:
    def __init__(self,data):
     self.data = data
     self.ref = None
class LinkedList:
    def __init__(self):
     self.head = None
 #checking if the linked list is empty   
    def print_LL(self):
       if self.head is None:
         print("Linked list is empty") 
#defining next node and data and stopping itteration   
       else:
            n = self.head
            while n is not None:
               print(n.data)
               n = n.ref
   
LL1 = LinkedList()
LL1.print_LL()