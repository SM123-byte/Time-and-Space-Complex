s = int(input("Enter the smallest number: "))
l = int(input("Enter the largest number: "))

lcm = l

while lcm % s != 0:
    lcm += l

print(lcm)