# Zeros vs Ones

N = int(input("Enter a number: "))

def determine_weight(binary_str):
    num_zeros = 0
    num_ones = 0

    for c in binary_str:
        if c == '0':
            num_zeros += 1
        else:
            num_ones += 1
    
    if num_zeros > num_ones:
        print("light")
    elif num_zeros < num_ones:
        print("heavy")
    elif num_zeros == num_ones:
        print("balanced")

def convert_to_binary(N):
    res = ""
    if N <= 0: print("Pick number above 0")

    while N > 0:
        res += str(N % 2)
        N //= 2
    print(res[::-1])
    determine_weight(res[::-1])

convert_to_binary(N)