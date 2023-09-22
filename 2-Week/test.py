# number = int(input("Enter Number: "))
# base = int(input("Enter Base: "))
# res = ""

# while number != 0:
#     res += str(number % base)
#     number = number // base

# print(''.join(reversed(res)))

s = input("Enter strings: ")
b = int(input("Enter Base: "))

n = 0
for c in s:
    n = b * n + int(c)

print(n)