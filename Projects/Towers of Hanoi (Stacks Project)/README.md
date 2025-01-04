<h1>Towers of Hanoi</h1>

<h2>Description</h2>

<h4>The game operates under the following rules:</h4>

• Single disk movement per turn
• Upper disks can only be placed on larger disks or empty rods
• Disks must be moved between rods one at a time

<h2>Rules</h2>
To solve the puzzle:
1. Move the entire stack of disks from the starting rod to a target rod
2. Only one disk can be moved at a time
3. No larger disk may be placed on top of a smaller disk

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