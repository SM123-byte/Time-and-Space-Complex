Large = int(input("Enter largest number: "))
Small = int(input("Enter smallest number: "))

while Small:
    store = Small
    Small = Large % Small
    Large = store

print(f"HCF is {Large}") 