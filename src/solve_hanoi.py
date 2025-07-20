def solve_hanoi(n, source, target):
    """This function solves the Hanoi puzzle. To call it, it is necessary three parameters
    >n= is the number of disks, must be a positive integer (future, it'll work with q1 and q2 functions)
    >source= is the source tower and must be 1, 2 or 3
    >target= is the target tower of the puzzle and must be 1,2, or 3 also.
    The return of this function will be a string that show the step by step on how to solve the puzzle,
    moving the disks accordingly"""
    
    assert isinstance(n, int) and n>=0, "Number of disks must be a positive integer."
    assert source in {1, 2, 3}, "Source tower number must be 1, 2, or 3."
    assert target in {1, 2, 3}, "Target tower number must be 1, 2, or 3."

    if n == 0:
        return ""

    spare= 6-source-target

    disks_to_spare=solve_hanoi(n-1, source, spare)
    last_disk=f"Move disk {n} from tower {source} to tower {target}.\n"
    disks_to_target=solve_hanoi(n-1, spare, target)

    return disks_to_spare+last_disk+disks_to_target
