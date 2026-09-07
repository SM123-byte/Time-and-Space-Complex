number = int(input("Enter your number: "))

original = number
reversed = 0

while number > 0:
    digit = number % 10
    reversed = reversed * 10 + digit
    number //= 10

if original == reversed:
    print("It is a palindrome")
else:
    print("It's not a palindrome")