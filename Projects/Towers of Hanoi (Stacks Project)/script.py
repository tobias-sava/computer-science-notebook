# Towers of Hanoi (Codecademy Practice Project) - 01/04/2025 

from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# creating the stacks

stacks = []

# creating the stacks by calling the Stack class

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

# adding the stacks to the list

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)  

# setting up the game
# making while loop to check if num_disks < 3

num_disks = 0

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

num_optimal_moves = 2 ** num_disks - 1

print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()

# getting user input

def get_input():

    choices = [stack.get_name()[0] for stack in stacks]

    # keep looping until valid input is received
    while True:
        # iterate through each stack
        for i in range(len(stacks)):
            # get the name of the current stack
            name = stacks[i].get_name()
            # get the letter of the current stack
            letter = choices[i]
            # print the letter and name of the current stack
            print(f"Enter {letter} for {name}")

        # get the user's choice
        user_input = input("")

        # if the user's choice is in the list of choices, return the choice
        if user_input in choices:
            return user_input
        
        # if user input is invalid, print error message
        print("\nInvalid Move. Try Again")

        # check if user input matches current choice
        if user_input == choices[i]:
            return stacks[i]


# playing the game

# initialize move counter
num_user_moves = 0

# continue until all disks are on right stack
while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    # display current state
    for stack in stacks:
        stack.print_items()
    
    while True:
        print("\nWhich stack do you want to move from?\n")
        # get source stack
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        # get destination stack
        to_stack = get_input()

        # check if source stack is empty
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again.")
        # check if move is valid
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            # move disk between stacks
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again.")

# print completion message with move counts

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))

# finished