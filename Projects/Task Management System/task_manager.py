# task management system - 01/08/2025

# creating this to further refine my knowledge on linked lists, queues and stacks

# creating linked list class

from task import Task # importing task class from task.py

# defining task manager class

class TaskManager:
    def __init__(self):
        self.head = None

    # implementing add task functionality

    def add_task(self, description):
        new_task = Task(description)

        # if list is empty, make task the head

        if self.head is None:
            self.head = new_task
            return
        
        # otherwise, traverse to the end of the list and add task there

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_task

    # implementing remove task functionality

    def remove_task(self, description):
        if self.head is None:
            print("No tasks to remove.")
            return False
        
        # if task to be removed is at the head:

        if self.head.description == description:
            self.head = self.head.next
            print(f"Task '{description}' removed.")
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.description == description:
                current.next = current.next.next
                print(f"Task '{description}' removed.")
                return True
            current = current.next
        print(f"Task '{description}' not found.")
        return False

# defining queue class

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, task):
        if self.rear is None:
            self.front = self.rear = task
            return
        self.rear.next = task
        self.rear = task
    
    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
            return None
        task = self.front
        self.front = self.front.next
        return task

# defining stack class

class Stack:
    def __init__(self):
        self.top = None

    # defining push functionality

    def push(self, task):
        task.next = self.top
        self.top = task

    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        task = self.top
        self.top = self.top.next
        return task

# to finish

# github.com/tobias-sava