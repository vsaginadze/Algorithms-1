from partition import partition

def qsort(a, lo, hi):
    if hi - lo <= 1:
        return
    
    k = partition(a, lo, hi)
    qsort(a, lo, k)
    qsort(a, k, hi)

def quicksort(a):
    qsort(a, 0, len(a))

quicksort([3, 4, 5, 1, 0, 2])