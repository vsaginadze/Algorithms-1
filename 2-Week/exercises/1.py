# Counting in Binary

N = int(input("Enter number: "))

def convert_to_binary(N):
    res = ""

    while N > 0:
        res += str(N % 2)
        N //= 2
    
    return res[::-1]

while N > 0:
    print(convert_to_binary(N))
    N -= 1