# Goldbach's Conjecture

n = int(input("Enter n: "))

def prime_sum(num, primes):
    for p1 in primes:
        for p in primes:
            if p+p1 == num:
                return f'{p1}+{p}={num}'

def is_sum_of_two_primes(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    primes = []
    
    for i in range(2, n):
        if prime[i]:
            primes.append(i)
            # cross off multiples of i
            for j in range(2*i, n, i):
                prime[j] = False

    for i in range(4, n+1, 2):
        print(prime_sum(i, primes))

is_sum_of_two_primes(n)