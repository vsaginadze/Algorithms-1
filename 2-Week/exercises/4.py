# Reverse the Digits
N = int(input("Enter number: "))
res = 0

while N > 0:
    d = N % 10
    N = N // 10
    res = res * 10 + d

print(res)