# from math import sqrt

# n = int(input("Enter number"))

# prime = [n] * True
# prime[0] = prime[1] = False

# pi = [0] * n
# count = 0

# for i in range(2, int(sqrt(n))+1):
#     if prime[i]:
#         count += 1
#         # cross off multiples of i
#         for j in range(i*i, n, i):
#             prime[j] = False
#     pi[i] = count

# from random import randint

# a = [randint(1, 1000) for i in range(0, 1000)]

# def binary_search(arr, num):
#     lo = 0
#     hi = len(arr) - 1

#     while lo <= hi:
#         midpoint = (lo + hi) // 2
#         if num == midpoint:
#             print(f'number is found {num}')
#         elif num > midpoint:
#             lo = midpoint + 1
#         else:
#             hi = midpoint - 1

a = [1,2,3,4,5,6,7,8]
k = 5
ans = None

# find first item that is >= k (ans = 5) 

lo = 0
hi = len(a) - 1

while lo <= hi:
    mid = (lo + hi) // 2
    if k > a[mid]:
        lo = mid + 1
    else:
        hi = mid - 1

print(a[lo])