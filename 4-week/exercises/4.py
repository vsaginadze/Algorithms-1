# Prime Experiment
from math import sqrt

n = 100

while True:
    prime = [True] * n 
    prime[0] = prime[1] = False
    for i in range(4, n):
        if prime[i]:
            # cross off multiples of i
            for j in range(2*i, n, i):
                prime[j] = False