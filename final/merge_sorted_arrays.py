def merge(a, b, c):
    i = j = 0 # index of a,b

    for k in range(len(c)):
        if j == len(b):
            c[k] = a[i]
            i += 1
        elif i == len(a):
            c[k] = b[j]
            j += 1
        elif a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
