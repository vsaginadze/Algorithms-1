def largest_val(arr):
    lo, hi = 0, len(arr)
    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] > arr[mid+1]:
            hi = mid-1
        else:
            lo = mid+1

    print(arr[lo])


    lo, hi = 0, len(nums)
    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] > nums[mid+1]:
            hi = mid-1
        else:
            lo = mid+1

    if target < lo:
        left = lo
        right = len(nums)-1
    else: 
        left = 0
        right = lo


    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:  # a[mid] > target
            right = mid - 1