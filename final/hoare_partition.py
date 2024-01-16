# objective: rearrange the elements in the range into two partitions a[lo:k]
# and a[k:hi] s.t. every element in first array is <= p and >= p in the second

# return k the index of the first element in second partition
def partition(a, lo, hi):
    p = a[lo]

    i = lo
    j = hi-1

    while True:
        while a[i] < p:
            i += 1
        while a[j] > p:
            j -= 1
        
        if j <= i:
            return j+1

        a[i], a[j] = a[j], a[i]

        i += 1
        j -= 1



a = [6, 5, 1, 3, 8, 7, 2, 4]
idx = partition(a, 0, 8)
print(a, idx)