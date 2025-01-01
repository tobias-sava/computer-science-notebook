# Static Arrays - 01/01/2025

# Python can simulate a static array (an array with fixed size) using a list, 
# but with predefined size constraints.

# creating a static array with the size of 5

static_array = [0] * 5 # initializing array with zeros

# accessing and modifying elements

static_array[0] = 10 # updating the first element of the list
static_array[4] = 20 # updating the last element of the list, -1 can also be used

# note; i already know my way around built in python arrays. i will soon
# practice more in a lower level language like cpp 

# printing the static array

print(static_array) # output: [10, 0, 0, 0, 20]

# enforcing static behaviour in python lists

# creating a simple class

class StaticArray:
    
    # defining starting traits (__init__)

    def __init__(self, size, initial_value=0):
        self.array = [initial_value] * size # creating fixed size array
        self.size = size

    def __getvalue__(self, index):
        return self.array[index]
    
    def __setvalue__(self, index, value):
        self.array[index] = value

    def __str__(self):
        return str(self.array)
    
# example usage

static_array = StaticArray(5)
static_array[0] = 10
static_array[0] = 20

print(static_array) # output: [10, 0, 0, 0, 20]

# in conclusion, with this approach, the array's size and behaviour remain 'static'.


