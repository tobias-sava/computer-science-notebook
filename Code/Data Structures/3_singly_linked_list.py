# Singly Linked List - 01/01/2025

# defining node class

class Node:
    def __init__(self, data):
        self.data = data # storing the data
        self.next = None # pointer to the next node

# defining linked list class

class SinglyLinkedList:
    def __init__(self):
        self.head = None # head of linked list

    # method for adding a node the end

    def append(self, data):
        new_node = Node(data)
        if not self.head: # if the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next: # traversing to the end of ll
            current = current.next
        current.next = new_node

    # method for adding a node to the beginning of ll

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head # pointing to the current head
        self.head = new_node

    # method for deleting node by value

    def delete(self, data):
        if not self.head: # if list is empty
            return
        if self.head.data == data: # if head node value == node (value) to delete
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data: # finding the node to delete
            current = current.next # moving onto next node
        if current.next: # if node is found
            current.next = current.next.next

    # method for printing ll

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# example usage
linked_list = SinglyLinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.prepend(5)
linked_list.display()  # output: 5 -> 10 -> 20 -> 30 -> None
linked_list.delete(20)
linked_list.display()  # output: 5 -> 10 -> 30 -> None