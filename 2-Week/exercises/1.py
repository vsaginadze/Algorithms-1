# Counting in Binary

N = int(input("Enter number: "))

def convert_to_binary(N):
    res = ""

    while N > 0:
        res = str(N % 2) + res
        N //= 2
    
    return res

while N > 0:
    print(convert_to_binary(N))
    N -= 1