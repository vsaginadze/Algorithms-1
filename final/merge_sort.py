from merge_sorted_arrays import merge

def merge_sort(a):
    if len(a) < 2:
        return

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, a)

a = [7, 3, 11, 8, 4]
merge_sort(a)
print(a)