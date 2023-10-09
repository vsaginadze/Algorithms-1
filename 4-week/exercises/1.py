# Largest Prime Gap

n = int(input("Enter n: "))

def largest_prime_gap(n):
    lpg = 0
    prev_prime = 0

    prime = [True] * n
    prime[0] = prime[1] = False

    for i in range(2, n):
        if prime[i]:
            if (i-prev_prime) > lpg:
                lpg = i - prev_prime

            prev_prime = i
            
            # cross off multiples of i
            for j in range(2*i, n, i):
                prime[j] = False

    print(lpg)

largest_prime_gap(n)