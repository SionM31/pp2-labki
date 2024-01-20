"""
 Write a program to solve a classic puzzle:

 We count 35 heads and 94 legs among the chickens and rabbits in a farm.

 How many rabbits and how many chickens do we have?

 create function: solve(numheads, numlegs):

 x + y = a
 2x + 4y = b

 b - 2a = 2y
 => y = (b - 2a) / 2
 = > x = a - y
"""

def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits

    print(f'There is {chickens} chickens and {rabbits} rabbits in a farm')

numheads, numlegs = map(int, input("Enter number of heads and legs in a farm: " ).split())
solve(numheads, numlegs)