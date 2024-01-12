def bubble_sort(arr):
    flag = len(arr) - 1

    while flag != 0:
        for i in range(flag):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag -= 1

arr = [5, 3, 1, 7, 2]
print(bubble_sort(arr))
