#test 241p week2
from code2 import *
def test_binarySearchFIrst(array, target):
    alist = [1, 2, 3, 4, 4, 5, 6]
    assert binarySearchFirstLast(alist, 4) == [3, 4]
    blist = []
    assert binarySearchFirstLast(alist, 4) == [-1, -1]

