# Used basic methods of converting 

decimal = int(input("Enter a number to convert: "))
binary = ""

if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        remain = decimal % 2
        binary = str(remain) + binary
        decimal = decimal // 2
print(binary)
