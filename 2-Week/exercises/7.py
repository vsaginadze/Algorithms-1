# Bertrand's postulate
from math import sqrt

def is_prime(n):
    prime = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            prime = False
            break

    return prime

n = int(input("Enter n: "))
count = 0
print("Primes: ", end="")
for num in range(n, 2*n+1):
    if is_prime(num):
        print(num, end=" ")
        count += 1

print(f"\nThere are {count} prime numbers between {n} and {2*n}")