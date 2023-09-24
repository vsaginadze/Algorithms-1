# Largest Prime Factor
from math import sqrt

n = int(input("Enter n: "))
f = 2

print(f"The largest prime factor of {n} is ", end="")
while f <= int(sqrt(n)):
    if n % f == 0:
        n //= f
    else:
        f += 1

print(n)