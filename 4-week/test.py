from math import sqrt

n = int(input("Enter number"))

prime = [n] * True
prime[0] = prime[1] = False

pi = [0] * n
count = 0

for i in range(2, int(sqrt(n))+1):
    if prime[i]:
        count += 1
        # cross off multiples of i
        for j in range(i*i, n, i):
            prime[j] = False
    pi[i] = count