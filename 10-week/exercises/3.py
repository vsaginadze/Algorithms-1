def valid_heap(arr):
    for i in range(len(arr), 3):
        left, right, val = arr[2*i + 1], arr[2*i + 2], arr[i]
        
        if not parent_is_greater(val, left, right):
            return False
        
    if not is_complete(arr):
        return False

    return True

def parent_is_greater(parent, left, right):
    if parent > left or parent > right:
        return False
    return True

def is_heap_complete(arr):
    depth, idx = max_depth(arr)
    num_of_items = 2**depth

    if len(arr[idx:]) == num_of_items or (num_of_items-1) == len(arr[idx:]):
        return True
    return False

def is_complete(arr):
    depth, idx = max_depth(arr)
    
    num_of_items = 2**depth

    if len(arr[idx:]) == num_of_items or (num_of_items-1) == len(arr[idx:]):
        return True
    return False

def max_depth(arr):
    depth, left = 0, 0
    while left < len(arr) and arr[left] is not None:
        left = 2*left + 1
        depth += 1
    return (depth - 1, (left-1)//2)
    
arr = [2, 5, 3, 11, 7, 6, 4, 14, 12, 10, 9, 13, 6, 8]

if valid_heap(arr):
    print("Valid heap")
else:
    print("Invalid heap")