number = int(input("Enter Number: "))
base = int(input("Enter Base: "))
res = ""

while number != 0:
    res += str(number % base)
    number = number // base

print(''.join(reversed(res)))