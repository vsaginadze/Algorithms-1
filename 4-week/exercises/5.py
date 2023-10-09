# Missing Number

def findMissingNumber(arr):
    left, right = 1, len(arr) + 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid - 1] == mid:
            left = mid + 1
        else:
            right = mid

    return left