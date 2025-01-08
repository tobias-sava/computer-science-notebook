<h1>Towers of Hanoi</h1>

<h2>Description</h2>

The Towers of Hanoi is a classic mathematical puzzle that consists of three rods and a number of disks of different sizes which can slide onto any rod. The puzzle starts with the disks neatly stacked in ascending order of size on one rod, creating a conical shape. The objective is to move the entire stack to another rod while following specific rules.

This puzzle was invented by the French mathematician Édouard Lucas in 1883. A legend says that in a temple in Hanoi, monks are attempting to move a stack of 64 golden disks according to these rules. According to the legend, when they complete the puzzle, the world will end.

<h2>Rules</h2>

To solve the puzzle:

1. Move the entire stack of disks from the starting rod to a target rod
2. Only one disk can be moved at a time
3. No larger disk may be placed on top of a smaller disk
4. Disks can only be moved if they are the topmost disk on a stack
5. The puzzle is complete when all disks are stacked in ascending order on the target rod

<h2>Implementation</h2>

Key technical components:

- Uses Stack data structure for each rod
- Implements recursive solution algorithm
- Time Complexity: O(2^n)
- Space Complexity: O(n)

<h2>Conclusion</h2>

This implementation demonstrates:

- Recursive problem-solving
- Stack data structures
- Minimum moves required = 2^n - 1

github.com/tobias-sava