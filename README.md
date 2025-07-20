# Hanoi-Puzzle
A simple Python command-line program to solve the Towers of Hanoi puzzle for 1 to 9 disks.

# Towers of Hanoi
The Towers of Hanoi is a classic mathematical puzzle that consists of three rods and a number of disks of different sizes which can slide onto any rod. The puzzle starts with the disks stacked in ascending order of size on one rod, the smallest disk on top. The objective is to move the entire stack to another rod, obeying the following rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on
top of another stack or on an empty rod.
3. No larger disk may be placed on top of a smaller disk.

If you want to try it out, you can find a live version of the puzzle at [Towers of Hanoi](https://www.mathsisfun.com/games/towerofhanoi.html).



## Features

- Prompts the user to enter the number of disks (between 1 and 9).
- Validates user input to ensure it is an integer in the allowed range.
- Prints a step-by-step solution to move all disks from the source tower to the target tower.

## How to Run

1. Make sure you have Python 3 installed.
2. Open a terminal in the `src` directory.
3. Run the main program:

   ```sh
   python hanoi.py
4. Follow the prompts to enter the number of disks.

# Project Structure
src/hanoi.py — Main entry point; handles user interaction and prints the solution.
src/solve_hanoi.py — Contains the recursive function to solve the puzzle.
src/validation_1_to_9.py — Input validation utilities.

# Example Output
Hello!
Let's solve the Towers of Hanoi puzzle! How many disks?
Enter an integer from 1 to 9: 3
___________________________________
Solution steps:
Move disk 1 from tower 1 to tower 3.
Move disk 2 from tower 1 to tower 2.
Move disk 1 from tower 3 to tower 2.
Move disk 3 from tower 1 to tower 3.
Move disk 1 from tower 2 to tower 1.
Move disk 2 from tower 2 to tower 3.
Move disk 1 from tower 1 to tower 3.
___________________________________
All disks have been moved from tower 1 to tower 3.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
You can edit or expand this as needed!  