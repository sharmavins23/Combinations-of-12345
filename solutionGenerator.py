import itertools


# Generate all possible r-combinations of a list of numbers.
def generateCombos(lst, r):
    # Basically, compute the rth dimensional cross product of the list
    if r == 0:
        return [[]]
    if r == 1:
        return [[i] for i in lst]

    combos = lst
    for _ in range(r-1):
        newLst = []

        # Iterate through all values in the new
        for aVal in combos:  # Might be a list
            # Iterate through all values in the original list
            for bVal in lst:  # Definitely is not a list
                if type(aVal) != list:
                    newLst.append([aVal] + [bVal])  # Add the two values
                else:
                    newLst.append(aVal + [bVal])  # Add the value to the list

        # After this, combos has a new list
        combos = newLst

    return combos


# Convert a list of digits to a single number.
def convertToNumber(lst):
    digitCounter = len(lst) - 1
    num = 0

    for digit in lst:
        num += digit * (10 ** digitCounter)
        digitCounter -= 1

    return num


# For a list of lists, convert each list to a single number.
def convertListToNumbers(lst):
    return [convertToNumber(lst[i]) for i in range(len(lst))]


# Check if a number is even.
def isEven(n):
    return n % 2 == 0


# Check if all digits in a number are different.
def isAllDifferent(n):
    return len(set(str(n))) == len(str(n))
