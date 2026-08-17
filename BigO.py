n = 10

guess = input("Double loop at n = 10 checks n x n pairs. How many? ")
input("Formula: one calculation, done. Please press enter to run ")
steps = 1
print(" steps=", steps, " -> O(1) constant time -> steps never change")

input("Loop: one step per item. Press enter to run ")
steps = 0
for i in range(n):
    steps += 1
print(" steps= ", steps, " -> O(n) linear time -> steps grow with n")

input("Double loop: checks every pair. Press enter to run ")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print(" steps=", steps, " your gues:", guess, " -> O(n^2) quadratic time")

input("Two more notations. Press enter ")
print(" Big Omega -> best case lower bound")
print(" Big Theta  -> exact bound (worst = best)")