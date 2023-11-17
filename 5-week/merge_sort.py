from merge import merge

def merge_sort(a):
    if len(a) < 2:
        return

    mid = len(a) // 2

    left = a[:mid]
    right = a[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, a)
    return a

a = [3, 1, 0, 2, 7, 5, 6]
print(merge_sort(a))