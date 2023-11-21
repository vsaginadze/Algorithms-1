from partition import partition

def qsort(a, lo, hi):
    if hi - lo <= 1:
        return
    
    k = partition(a, lo, hi)
    qsort(a, lo, k)
    qsort(a, k, hi)

def quicksort(a):
    qsort(a, 0, len(a))

quicksort([6, 5, 1, 3, 8, 7, 2, 4])