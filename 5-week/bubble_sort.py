def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

'''
What's the running time of bubble sort? Suppose that the input array has N elements. 
As mentioned above, on the first pass we make (N – 1) comparisons; 
on the second pass we make (N – 2) comparisons, and so on. The total number of comparisons is

(N – 1) + (N – 2) + … + 2 + 1 = N(N – 1) / 2 = O(N2)
'''