from solutionGenerator import generateCombos
from solutionGenerator import convertToNumber
from solutionGenerator import convertListToNumbers
from solutionGenerator import isEven
from solutionGenerator import isAllDifferent


# Test generateCombos(lst, r)
def testGenerateCombos():
    lst = [1, 2, 3]
    r = 2
    correct = [[1, 1], [1, 2], [1, 3],
               [2, 1], [2, 2], [2, 3],
               [3, 1], [3, 2], [3, 3]]
    assert generateCombos(lst, r) == correct

    lst = [1, 2, 3, 4, 5]
    r = 2
    correct = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5],
               [2, 1], [2, 2], [2, 3], [2, 4], [2, 5],
               [3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
               [4, 1], [4, 2], [4, 3], [4, 4], [4, 5],
               [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
    assert generateCombos(lst, r) == correct


# Test convertToNumber(lst)
def testConvertToNumber():
    lst = [1, 2, 3]
    correct = 123
    assert convertToNumber(lst) == correct

    lst = [1, 2, 3, 4, 5]
    correct = 12345
    assert convertToNumber(lst) == correct


# Test convertListToNumbers(lst)
def testConvertListToNumbers():
    lst = [[1, 2, 3], [4, 5, 6]]
    correct = [123, 456]
    assert convertListToNumbers(lst) == correct


# Test isEven(n)
def testIsEven():
    assert isEven(0) == True
    assert isEven(1) == False
    assert isEven(2) == True
    assert isEven(3) == False
    assert isEven(4) == True
    assert isEven(5) == False


# Test isAllDifferent(n)
def testIsAllDifferent():
    assert isAllDifferent(0) == True
    assert isAllDifferent(1) == True

    assert isAllDifferent(12) == True
    assert isAllDifferent(13) == True

    assert isAllDifferent(33) == False
    assert isAllDifferent(34) == True

    assert isAllDifferent(123) == True
    assert isAllDifferent(124) == True

    assert isAllDifferent(12324523) == False


if __name__ == '__main__':
    # Run basic function tests
    testGenerateCombos()
    testConvertToNumber()
    testConvertListToNumbers()
    testIsEven()
    testIsAllDifferent()

    print("Everything passed.")
