Dynamic and Static Arrays - 01/01/2025

-

! Static Arrays

A static array is a type of array with the following key characteristics:

1) Fixed Size: Its size is determined when it’s created and cannot change later.

Example: If you make an array to hold 5 items, it will always have space for exactly 5 items.

2) Contiguous Memory: All the elements are stored next to each other in memory.

3) Fast Access: You can quickly access any element by its index because the memory layout is predictable (O(1) for access).


Use cases:

1) Storing and accessing sequential data.

2) Temporarily storing objects.

3) Used by IO routines as buffers.

4) Lookup tables and inverse lookup tables.

5) Can be used to return multiple values from a function.

6) Used in dynamic programming to cache answers to subproblems.

-

Complexity:

Access 0(1) / 0(1)

Search 0(n) / 0(n)

Insertion N/A / 0(n)

Appending N/A / 0(1)

Deletion N/A / 0(n)

-

A = [44, 12, -5, 17, 6, 0, 3, 9, 100]

Index = [0, 1, 2, 3, 4, 5, 7 etc...]

Example: Value 44 in our static array is equal to Index[0].

Example: Index[500] == Index out of bounds (program will throw an exception/error
because the index does not exist)

Computer science is mainly, if not all, zero-based. Unlike mathematics.

-

! Dynamic Arrays

A dynamic array is an array that can grow or shrink in size as needed. 
Unlike static arrays, it doesn’t have a fixed size—it adjusts automatically when you add or remove items.

Example of a dynamic array in Python:

    # Create a dynamic array
    dynamic_array = []

    # Add elements (the array grows automatically)
    dynamic_array.append(1)
    dynamic_array.append(2)
    dynamic_array.append(3)

    print(dynamic_array)  # Output: [1, 2, 3]

    # Remove elements (the array shrinks if needed)
    dynamic_array.pop()
    print(dynamic_array)  # Output: [1, 2]

    # Access elements
    print(dynamic_array[0])  # Output: 1

Languages like Python handle all the resizing and memory behind the scenes, 
but in lower-level languages like C and C++, you need to build and manage the 
dynamic behavior yourself. This gives you more control but requires more work!

Example of a dynamic array in CPP:

#include <iostream>

    int main() {
        int initialSize = 2;
        int* arr = new int[initialSize]; // Manually allocate memory
        int currentSize = 0;

        // Add elements (resize if needed)
        for (int i = 0; i < 5; i++) {
            if (currentSize == initialSize) {
                // Resize array
                int newSize = initialSize * 2;
                int* newArr = new int[newSize];
                for (int j = 0; j < currentSize; j++) {
                    newArr[j] = arr[j];
                }
                delete[] arr; // Free old memory
                arr = newArr;
                initialSize = newSize;
            }
            arr[currentSize++] = i + 1;
        }

        // Print elements
        for (int i = 0; i < currentSize; i++) {
            std::cout << arr[i] << " ";
        }

        delete[] arr; // Free memory
        return 0;
    }


-

Complexity

// Static Array
Access: O(1)         // Getting/setting element at index
Search: O(n)         // Finding element in array
Traverse: O(n)       // Going through all elements
Length: O(1)         // Getting array size
Insert: N/A          // Cannot insert in static array
Remove: N/A          // Cannot remove from static array

// Dynamic Array
Access: O(1)         // Getting/setting element at index
Search: O(n)         // Finding element in array
Traverse: O(n)       // Going through all elements
Length: O(1)         // Getting array size
Append: O(1)*        // Adding to end of array
Insert: O(n)         // Adding at specific position
Remove: O(n)         // Removing element
Clear: O(1)          // Removing all elements

*Amortized O(1) - occasional O(n) when resizing







