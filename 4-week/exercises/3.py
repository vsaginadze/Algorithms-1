# Random Array

'''
Write a program that reads an integer N and generates a random array of N integers in ascending order. 
The first number in the array should be 0, and the difference between each pair of consecutive array elements 
should be a random number from 1 to 10.

diff = randint(1, 10)
while diff < prev_diff:
    diff = randint(1, 10)

arr[i+1] = arr[i] + diff

'''
from random import randint
n = int(input("Enter N: "))
arr = [0]
diff = randint(1, 10)

for i in range(0, n-1):
    arr.append(arr[i]+diff)
    if diff != 10:
        prev_diff = diff
        diff = randint(1, 10)
        while diff < prev_diff:
            diff = randint(1, 10)
            
arr1 = [randint(1, 10) * 10 for i in range(n)]

for el in arr1:
    if el in arr:
        print(f'{el} is in the array')