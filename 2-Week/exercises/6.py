# Prime Optimization
from math import sqrt

n = int(input('Enter n: '))

prime = True
for i in range(2, int(sqrt(n)) // 2 + 1):
    if n % i == 0:
        prime = False
        break

if prime:
    print('n is prime')
else:
    print('not prime')