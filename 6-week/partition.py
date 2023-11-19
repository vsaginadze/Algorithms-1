# We are given an unsorted range a[lo:hi] to be partitioned, with
# hi - lo >= 2 (i.e. at least 2 elements in the range).
#
# Choose a pivot value p, and rearrange the elements in the range into
# two partitions p[lo:k] (with values <= p) and p[k:hi] (with values >= p).
# Both partitions must be non-empty.
#
# Return k, the index of the first element in the second partition.
def partition(a, lo, hi):
    # For now, choose the first element as the pivot.
    # Warning: This may be inefficient; see the discussion below.
    p = a[lo]

    i = lo
    j = hi - 1

    while True:
        # Look for two elements to swap
        while a[i] < p:
            i += 1
        while a[j] > p:
            j -= 1
        
        if j <= i: # Nothing to swap
            return j + 1
    
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1