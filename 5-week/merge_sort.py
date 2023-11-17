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

a = [4, -1, 5, 0, 7, -5]
print(merge_sort(a))