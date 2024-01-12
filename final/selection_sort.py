def selection_sort(arr):
    first_unsorted_idx = 0

    while first_unsorted_idx < len(arr):
        min_idx = first_unsorted_idx

        for idx in range(first_unsorted_idx, len(arr)):
            if arr[idx] < arr[min_idx]:
                min_idx = idx

        arr[first_unsorted_idx], arr[min_idx] = arr[min_idx], arr[first_unsorted_idx]
        first_unsorted_idx += 1



arr = [5, 3, -1, 2, -2, 5]
print(selection_sort(arr))
