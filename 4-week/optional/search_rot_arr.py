def searchRange(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            b_left = mid
            b_right = mid

        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1

print(searchRange([-3,-2,-1,0,1,3,4,5,7,7,8,8,10], -1))

# ? - erti zgvari rcheba ucvleli