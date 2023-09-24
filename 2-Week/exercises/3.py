# Base 7 to Base 3

num_base7 = input("Enter number in base 7: ")[::-1]
num_int = 0
res = ""

for i in range(len(num_base7)):
    num_int += int(num_base7[i]) * 7 ** i

while num_int != 0:
    res += str(num_int % 3)
    num_int //= 3

print(res[::-1])