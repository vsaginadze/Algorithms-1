def insertion_sort(arr):
    for i in range(1, len(arr)):
        t = arr[i]
        j = i-1
        while j >= 0 and arr[j] > t:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = t
    return arr

arr = [-2, 5, 3, 1, -56, 7, 2, -3]
print(insertion_sort(arr))