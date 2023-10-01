def calc_gcd(a,b):
    while b > 0:
        a, b = b, a % b

    return a

a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))

c = int(input("Enter numerator: "))
d = int(input("Enter denominator: "))

numerator = None

# 1. calculate denominators using LCM
denominator = b * d // calc_gcd(b, d)

# 2. Divide LCM on first and second denominator
q1, q2 = denominator // b, denominator // d

# 3. multiply each quotent respectively on numerators
a, c = a*q1, c*q2

# 4. add numerators
numerator = a + c

# 5. reduce fraction using GCD
gcd = calc_gcd(numerator, denominator)
numerator = numerator // gcd
denominator = denominator // gcd

print(f"Answer: {numerator}/{denominator}")