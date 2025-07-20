def is_1_to_9(n):
    """This function will analyse a parameter n (an integer) and return a boolean response,
    If n is in 1 to 9, will show True. If not, n will be False"""
    if str(n) in map(str, range(1,10)):
        return True
    else:
        return False

def prompt_1_to_9():
    """For this function, it is necessary to import function is_1_to_9() from q1.py file.
    This prompt will ask an input from the user that's an integer between 1 to 9, using is_1_to_9.
    If the user type a number outside these parameter, the function will prompt Invalid Input and make
    recursive call to the function itself, until it's given a proper input. """

    n_disk=input("Enter an integer from 1 to 9: ")

    if is_1_to_9(n_disk):
        return int(n_disk)
    
    print('Invalid input.')
    return prompt_1_to_9()

