# Most Repeated Factor
from math import sqrt

n = int(input("Enter n: "))

def is_prime(n):
    prime = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
                prime = False
                break
    return prime

most_frequent = None
max_count = 0
f = 2

while f <= int(sqrt(n)):
    if n % f == 0 and is_prime(f):
        count = 0
        while n % f == 0:
            count +=1 
            n //= f
        if max_count < count:
            max_count = count
            most_frequent = f
    f += 1

print(most_frequent)
