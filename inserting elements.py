class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_after_node(self, node, data):
        if node is None:
            print("Previous node is not found.")
            return
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)


# Create an empty linked list
my_list = LinkedList()

# Insert elements into the linked list
my_list.insert_at_end(10)
my_list.insert_at_end(20)
my_list.insert_at_end(30)
my_list.insert_at_beginning(5)
my_list.insert_after_node(my_list.head.next, 15)

# Display the linked list
my_list.display()  # Output: [5, 10, 15, 20, 30]
