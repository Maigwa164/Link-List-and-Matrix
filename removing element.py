class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_element(self, data):
        if self.is_empty():
            print("Linked list is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print("Element not found in the linked list.")

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)


# Create a linked list
my_list = LinkedList()

# Insert elements into the linked list
my_list.insert_at_end(10)
my_list.insert_at_end(20)
my_list.insert_at_end(30)
my_list.insert_at_end(40)

# Display the linked list
my_list.display()  # Output: [10, 20, 30, 40]

# Remove an element from the linked list
my_list.remove_element(20)

# Display the updated linked list
my_list.display()  # Output: [10, 30, 40]
