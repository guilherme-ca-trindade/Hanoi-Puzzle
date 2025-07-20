from solve_hanoi import *
from validation_1_to_9 import *

def hanoi():
    print("Hello!")
    print("Let's solve the Towers of Hanoi puzzle! How many disks?")

    n_disks=prompt_1_to_9()

    solution=solve_hanoi(n_disks,1,3)
    print("_"*35)
    print("Solution steps:")
    print(solution)


hanoi()
