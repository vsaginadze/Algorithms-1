def largest_val(arr):
    lo, hi = 0, len(arr)
    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] > arr[mid+1]:
            hi = mid-1
        else:
            lo = mid+1

    print(arr[lo])
