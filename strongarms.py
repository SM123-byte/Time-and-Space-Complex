# An Armstrong number is a number of where all of its digits is expononent to the number of digits and adds up to it; for example 153 --> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
number = int(input("Enter your number: "))

digits = len(str(number))

resultNumber = 0

temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //= 10

if number == resultNumber:
    print(number, "is an armstrong number")
else:
    print(number, "is not an armstrong number")