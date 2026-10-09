#Task 1
def binarySearchFirst(array, target):
    lo = 0
    hi = len(array)-1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] < target:
            lo = mid + 1
        elif array[mid] > target:
            hi = mid - 1
        else:
            result = mid
            hi = mid - 1
    return result
    

def binarySearchLast(array, target):
    lo = 0
    hi = len(array)-1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] < target:
            lo = mid + 1
        elif array[mid] > target:
            hi = mid - 1
        else:
            result = mid
            lo = mid + 1
        return result

def binarySearchFirstLast(array, target):
    alist = []
    alist.append(binarySearchFirst(array, target))
    alist.append(binarySearchLast(array, target))
    return alist
array = [1, 2, 4, 5, 5, 5, 6, 7]
target = 5
print(binarySearchFirstLast(array, target))