# Towers of Hanoi

# The Towers of Hanoi is a classic problem that involves moving a stack of disks from one pole to another using an intermediate pole, subject to the constraints that only one disk can be moved at a time and a larger disk cannot be placed on top of a smaller disk. Here's a sample implementation of the Towers of Hanoi using Python:

def towers_of_hanoi(n, from_pole, to_pole, aux_pole):
    if n == 1:
        print(f"Move disk 1 from {from_pole} to {to_pole}")
        return
    towers_of_hanoi(n-1, from_pole, aux_pole, to_pole)
    print(f"Move disk {n} from {from_pole} to {to_pole}")
    towers_of_hanoi(n-1, aux_pole, to_pole, from_pole)

# Example usage
towers_of_hanoi(3, 'A', 'C', 'B')

#In the above code, the towers_of_hanoi function takes three arguments: n (the number of disks), from_pole (the starting pole), to_pole (the destination pole), and aux_pole (the intermediate pole). The base case is when there is only one disk, in which case we simply move it from the starting pole to the destination pole. For the recursive case, we first move n-1 disks from the starting pole to the intermediate pole using the destination pole as the auxiliary pole. We then move the remaining disk from the starting pole to the destination pole, and finally move the n-1 disks from the intermediate pole to the destination pole using the starting pole as the auxiliary pole.

#When we run the above code with towers_of_hanoi(3, 'A', 'C', 'B'), the output will be:

Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C



