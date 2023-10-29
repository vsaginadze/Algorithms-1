def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        min_idx = i
        min_val = a[i]
        for j in range(i+1, n):
            if a[j] < min_val:
                min_val = a[j]
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    
    return a
    
print(selection_sort([2,3,4,-1,2,0]))