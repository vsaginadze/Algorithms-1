def search(nums, target):
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    if len(nums) == 2:
        if nums[0] == target:
            return 0
        elif nums[1] == target:
            return 1
        else:
            return -1

    is_pivot = True
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid == len(nums)-1:
            right = len(nums)-1
            left = 0
            is_pivot = False
            break
        if nums[mid] > nums[mid+1]:
            hi = mid-1
        else:
            lo = mid+1

    if is_pivot:
        if target <= nums[lo+1]:
            left = lo+1
            right = len(nums)-1
        else:
            left = 0
            right = lo
    else:
        left, right = 0, len(nums)-1

    print(left, right, is_pivot)
    print(nums[left], nums[right])
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(search([5, 1, 3], 5))
