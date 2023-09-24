# Nth Prime
from math import sqrt

def is_prime(n):
    prime = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            prime = False
            break
    return prime

n = int(input("Enter n: "))
num = 2
count = 1

while True:
    if is_prime(num):
        if n == count:
            print(f"The {n} prime number is {num}")
            break
        count += 1
    num += 1