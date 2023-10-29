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

'''
a -> [4, -1, 5, 0, 7, -5] 
if 6 < 2:
    return

mid = 3 -> 6 // 2 = 3
left = [4, -1, 5] -> a[:3]
right = [0, 7, -5] -> a[3:]

merge_sort([4, -1, 5])
    a -> [4, -1, 5]
    if 3 < 2:
        return
    
    mid = 1 -> 3 // 2
    left = [4] -> a[:1]
    right = [-1, 5] -> a[1:]

    merge_sort([4])
        a -> [4]
        if 1 < 2:
            return
    merge_sort([-1, 5])
        a -> [-1, 5]

        if 2 < 2:
            return
        
        mid = 1 -> 2 // 2
        left = [-1]
        right = [5]

        merge_sort([-1])
            a -> [-1]
            if 1 < 2:
                return
        merge_sort([5])
            a -> [5]
            if 1 < 2:
                return

        merge([-1], [5], [-1, 5])
    
    merge([4], [-1, 5], [4, -1, 5]) -> [-1, 4, 5]

merge_sort([0, 7, -5])
if 3 < 2:
    return

mid = 1
left = [0]
right = [7, -5]

merge_sort([0]) -> [0]

merge_sort([7, -5])
    if 2 < 2:
        return
    
    mid = 1
    left = [7]
    right = [-5]

    merge_sort([7]) -> return
    merge_sort([-5]) -> return

    merge([7], [-5], [7, -5]) -> [-5, 7]

merge([0], [-5, 7], a) -> [-5, 0, 7]

merge([-1, 4, 5], [-5, 0, 7]) -> [-5, -1, 0, 4, 5, 7]



'''

'''
recursive functions attempt to convert each splitted array into sorted one
    * it does it by splitting the array in half until the size of array reaces one
    * than merges arrays into sorted ones and builds from there
    
than merge tham into one sorted array
'''