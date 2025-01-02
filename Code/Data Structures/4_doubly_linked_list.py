# Doubly Linked List - 01/01/2025

class Node: 
    def __init__(self, data):
        self.data = data # storing data
        self.next = None # pointer to next node
        self.prev = None # pointer to prev node

class DoublyLinkedList:
    def __init__(self):
        self.head = None # head of the linked list

    # method for adding node at the end

    def append(self, data):
        new_node = Node(data)
        if not self.head: # if the list is empty
            self.head = new_node
            return
        current = self.headw
        while current.next: # traversing to the end
            current = current.next # going to next node
        current.next = new_node
        new_node.prev = current

    # method for adding a node at the beginning

    def prepend(self, data):
        new_node = Node(data)
        if self.head: # if list is empty
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    # method for deleting a node by value

    def delete(self, data):
        if not self.head: # if list is empty
            return
        current = self.head
        if current.data == data: # if the head is the node to delete
            self.head = current.next
            if self.head: # updating the heads prev pointer
                self.head.prev = None
            return
        while current and current.data != data: # finding the node to delete
            current = current.next
        if current: # if the node is found
            if current.next: # if its not the last node
            current.next.prev = current.prev
        if current.prev: # if its not the first node
            current.prev.next = current.next

    # method for printing ll

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# example usage
linked_list = DoublyLinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.prepend(5)
linked_list.display()  # output: 5 <-> 10 <-> 20 <-> 30 <-> None
linked_list.delete(20)
linked_list.display()  # output: 5 <-> 10 <-> 30 <-> None 
