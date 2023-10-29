def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        t = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > t:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = t
    
    print(arr)

insertion_sort([2,3,4,5,-1,-2,0])