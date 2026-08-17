n = int(input("Enter any n (try 5, 10, or 50)"))

input(" One loop - runs once per item. Press enter to run")
for i in range(n):
    pass
print(" n=", n, " steps= ", n, "-> O(n) linear time")

input("Two nested loops - runs n x n times. Press enter to run ")
for i in range(n):
    for j in range(n):
        pass

print(" n=", n, " steps=", n * n, " -> O(n^2) quadratic time")

input("Rule: count the loops. Press enter to run")
print(" 0 loops -> O(1) 1 loop -> O(n) 2 nested -> O(n^2)")