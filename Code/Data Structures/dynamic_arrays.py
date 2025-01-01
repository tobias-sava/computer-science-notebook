# Dynamic Arrays - 01/01/2025

# dynamic arrays are already built into python (list function) however,
# to better understand its behaviour i will be creating a custom class

# creating dynamic array

dynamic_array = []

# adding elements

dynamic_array.append(10)
dynamic_array.append(20)
dynamic_array.append(30)

print(dynamic_array) # output: [10, 20, 30]

# removing elements

dynamic_array.pop()
print(dynamic_array)  # output: [10, 20]


# enforcing dynamic behaviour with a custom class:

class DynamicArray:
    def __init__(self):
        self.array = [None] * 1  # startubg with an array of size 1
        self.size = 0           # number of elements in the array
        self.capacity = 1       # total capacity of the array

    def append(self, value):
        if self.size == self.capacity:  # checkubg if resizing is needed
            self._resize(self.capacity * 2)
        self.array[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("pop from empty array")
        value = self.array[self.size - 1]
        self.size -= 1
        if self.size <= self.capacity // 4:  # shrink if necessary
            self._resize(self.capacity // 2)
        return value

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):  # copy existing elements
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        return self.array[index]

    def __str__(self):
        return str([self.array[i] for i in range(self.size)])

# example usage:
dynamic_array = DynamicArray()
dynamic_array.append(10)
dynamic_array.append(20)
dynamic_array.append(30)
print(dynamic_array)  # output: [10, 20, 30]

dynamic_array.pop()
print(dynamic_array)  # output: [10, 20]

