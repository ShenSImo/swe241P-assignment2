#test 241p week2
from code2 import *

def test_firstLast():
    assert binarySearchFirstLast([4, 9, 10, 13, 17, 17, 19, 21], 17) == [4, 5]
    assert binarySearchFirstLast([2, 4, 6, 8, 10, 14, 16], 12) == [-1, -1]
    assert binarySearchFirstLast([], 0) == [-1, -1]
    assert binarySearchFirstLast([5, 5, 5, 5], 5) == [0, 3]

def test_findMatrix():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert findMatrix(matrix, 3) == True
    assert findMatrix(matrix, 13) == False
    assert findMatrix([], 5) == False