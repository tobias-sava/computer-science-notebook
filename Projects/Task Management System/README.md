<h1>Task Management System</h1>

<h2>Description</h2>

The Task Management System is a simple application that allows users to manage tasks using basic data structures. The system employs a Linked List to store tasks, a Queue to manage regular tasks in a FIFO (First In, First Out) manner, and a Stack to handle high-priority tasks in a LIFO (Last In, First Out) manner. This project demonstrates the use of these fundamental data structures to build a functional task management system.

The system allows users to:

- Add tasks to the system
- Organize tasks into a priority (stack) or regular (queue) category  
- Process tasks in priority order
- Display current tasks stored in the system

<h2>Rules</h2>

To use the system:

1. Add tasks by specifying whether they are priority (stack) tasks or regular (queue) tasks
2. Only one task can be processed at a time
3. Priority tasks are processed before regular tasks
4. Tasks can be removed and marked as completed by removing them from the linked list
5. The task list is dynamic, and tasks are stored in a linked list structure

<h2>Implementation</h2>

Key technical components:

- Linked List: Used to store all tasks in the system
- Queue: Used to handle regular tasks that are processed in FIFO order
- Stack: Used to handle high-priority tasks processed in LIFO order
- TaskManager Class: Manages tasks using the above data structures and provides methods to add, remove, process, and display tasks

Time Complexity:

- Adding a task: O(1) for stack/queue, O(n) for linked list (in case of traversing)
- Removing a task: O(n) (because the task needs to be removed from the linked list)
- Processing tasks: O(1) for each task processed

Space Complexity:

- Linked List: O(n), where n is the number of tasks in the system
- Queue and Stack: O(m) and O(p) where m and p represent the number of tasks in the queue and stack, respectively

<h2>Conclusion</h2>

This implementation demonstrates:

- Recursive problem-solving for managing task processing order
- Understanding and applying stack, queue, and linked list data structures
- Managing task prioritization based on stack (high-priority) and queue (regular-priority) processing
