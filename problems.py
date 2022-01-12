from solutionGenerator import generateCombos
from solutionGenerator import convertListToNumbers
from solutionGenerator import isEven
from solutionGenerator import isAllDifferent


# Problem 1.a.
# How many permutations in total?
def problem1a():
    lst = [1, 2, 3, 4, 5]
    r = 4

    # Generate all possible r-permutations of lst
    perms = generateCombos(lst, r)

    return len(perms)


# Problem 1.b.
# How many permutations have all digits different?
def problem1b():
    lst = [1, 2, 3, 4, 5]
    r = 4

    # Generate all possible r-permutations of lst
    perms = generateCombos(lst, r)

    # Convert each permutation to a number
    perms = convertListToNumbers(perms)

    # Count the number of permutations that have all digits different
    count = 0
    for perm in perms:
        if isAllDifferent(perm):
            count += 1

    return count


# Problem 1.c.
# How many permutations have an even number of digits?
def problem1c():
    lst = [1, 2, 3, 4, 5]
    r = 4

    # Generate all possible r-permutations of lst
    perms = generateCombos(lst, r)

    # Convert each permutation to a number
    perms = convertListToNumbers(perms)

    # Count the number of permutations that have an even number of digits
    count = 0
    for perm in perms:
        if isEven(perm):
            count += 1

    return count


# Problem 1.d.
# How many permutations have both an even number of digits and all digits different?
def problem1d():
    lst = [1, 2, 3, 4, 5]
    r = 4

    # Generate all possible r-permutations of lst
    perms = generateCombos(lst, r)

    # Convert each permutation to a number
    perms = convertListToNumbers(perms)

    # Count the number of permutations that have an even number of digits
    count = 0
    for perm in perms:
        if isEven(perm) and isAllDifferent(perm):
            count += 1

    return count


if __name__ == "__main__":
    print("Problem 1.a:", problem1a())
    print("Problem 1.b:", problem1b())
    print("Problem 1.c:", problem1c())
    print("Problem 1.d:", problem1d())
