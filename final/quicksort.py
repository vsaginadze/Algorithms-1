from hoare_partition import partition

def qsort(a, lo, hi):
    if hi - lo <= 1:
        return
    
    k = partition(a, lo, hi)

    qsort(a, lo, k)
    qsort(a, k, lo)

qsort([3, 7, 0, 2], 0, 4)