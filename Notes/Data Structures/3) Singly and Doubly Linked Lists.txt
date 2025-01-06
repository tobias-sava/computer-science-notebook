Singly and Doubly Linked Lists - 01/01/2025

A linked list is a sequential list of nodes that hold data which point
to other nodes also containing data.

Where are linked lists used?

1) Used in many List, Queue and Stack implementations.

2) Great for creating circular lists.

3) Can easily model real world objects such as trains.

4) Used in separate chaning which is present in certain Hashtable implementations to
deal with hashing collisions.

5) Often used in the implementation of adjacency lists for graphs.


Terminology:

Head = The first node in a linked list.

Tail = The last node in a linked list.

Pointer = Reference to another node.

Node: An object containing data and pointer(s).

-

Singly vs Doubly Linked Lists

Singly linked lists contain 1 pointer to the next node.

Doubly linked lists contain 2 pointers;

1) Pointer to the next node.
2) Pointer to the previous node.


Pros and Cons:

Singly - Uses less memory, simpler implementation BUT cannot access previous elements easily.

Doubly - Can be traversed backwards BUT takes 2x memory.


-

! SINGLY LINKED LIST 

1. Adding an element:

    At the beginning:

        Create a new node.
        Point its next to the current head.
        Update head to the new node.

    At the end:

        Create a new node.
        Traverse to the last node (node.next == None).
        Point the last node’s next to the new node.

    At a specific position:

        Traverse to the node before the desired position.
        Update the new node’s next to the current node at that position.
        Update the previous node’s next to point to the new node.

2. Removing an element:

    From the beginning:

        Update the head to the second node (head.next).
        
    From the end:

        Traverse to the second-last node.
        Update its next to None.

    From a specific position:

        Traverse to the node before the target node.
        Update its next to skip the target node (node.next = node.next.next).

! DOUBLY LINKED LIST

1. Adding an element

    At the beginning:

        Create a new node.
        Set its next to the current head.
        Update the current head's prev to the new node.
        Update head to the new node.

    At the end:

        Create a new node.
        Traverse to the last node.
        Set the last node’s next to the new node.
        Set the new node’s prev to the last node.

    At a specific position:

Traverse to the node before the desired position.
Update the new node’s prev and next pointers to link with the surrounding nodes.
Update the surrounding nodes’ pointers.

2. Removing an element

    From the beginning:

    Update head to head.next.
    Set the new head's prev to None.

    From the end:

    Traverse to the second-last node.
    Set its next to None.

    From a specific position:

    Update the surrounding nodes' prev and next pointers to bypass the target node.

-

Complexity

// Singly Linked List
add_next_node: O(1)      // Adding after current node
add_head: O(1)          // Adding at beginning
add_tail: O(n)          // Adding at end (need to traverse)
remove_next: O(1)       // Removing after current node  
remove_head: O(1)       // Removing first node
remove_tail: O(n)       // Removing last node (need to traverse)
search: O(n)            // Finding a value
get_size: O(1)         // Getting list size
is_empty: O(1)         // Checking if empty

// Doubly Linked List  
add_next_node: O(1)     // Adding after current node
add_prev_node: O(1)     // Adding before current node
add_head: O(1)         // Adding at beginning
add_tail: O(1)         // Adding at end (have tail pointer)
remove_node: O(1)      // Removing current node
remove_head: O(1)      // Removing first node
remove_tail: O(1)      // Removing last node
search: O(n)           // Finding a value
get_size: O(1)        // Getting list size
is_empty: O(1)        // Checking if empty


Rest of the studies regarding linked lists have been done on paper.
