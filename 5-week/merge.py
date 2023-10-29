def merge(a, b, c):
    i = j = 0

    for k in range(len(c)):
        if i == len(a):
            c[k] = b[j]
            j += 1
        elif j == len(b):
            c[k] = a[i]
            i += 1
        elif a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
    
    print(c)



a = [3, 5, 7, 10]
b = [-1, 6, 11]
c = (len(a) + len(b)) * [0]

merge(a, b, c)

'''
a and b are sorted
1. i and j tracks smallest elements of a and b respectively

2. if i hits len(a) there are no more smallest elements of a so we add smallest elements of b
3. same as step 2 in j
4. if a's smallest element is smaller than b's smallest element than add from a and increase the i(index of a smallest element of a)
5. if step 4 fails do same for b
'''