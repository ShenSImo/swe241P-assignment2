#test 241p week2
from code2 import *
def test_binarySearchFirst():
    alist = [1, 2, 3, 4, 4, 5, 6]
    assert binarySearchFirstLast(alist, 4) == [3, 4]
    blist = []
    assert binarySearchFirstLast(blist, 4) == [-1, -1]


def test_findMatrix():
    matrix = [[1, 3, 4], 
              [4, 5, 7], 
              [8, 9, 9] ]
    assert findMatrix(matrix, 5) == True
    assert findMatrix(matrix, 10) == False
    matrix = []
    assert findMatrix(matrix, 10) == False