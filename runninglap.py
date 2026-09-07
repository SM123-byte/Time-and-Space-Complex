# In this code we are going to be running pieces of code that will all give the same answer - we will try to find out the most efficient way of these codes.
n = 4

print("Using Formulae")
total_formula = n * (n + 1) // 2
steps_formula = 1

print(f"Total Points: {total_formula}")
print(f"Actual Steps: {steps_formula}\n")


print("Using Loop")
total_loop = 0
steps_loop = 0

for lap in range(1, n + 1):
    total_loop += lap
    steps_loop += 1  

print(f"Total Points: {total_loop}")
print(f"Actual Steps: {steps_loop}\n")

print("--- Method 3: Nested Loop Method ---")
total_nested = 0
steps_nested = 0

for lap in range(1, n + 1):
    for point in range(1, lap + 1):
        total_nested += 1
        steps_nested += 1 

print(f"Total Points: {total_nested}")
print(f"Actual Steps: {steps_nested}\n")

print("After running all the pieces of codee we have found that using a formula is the most efficient way of finding out the answer to the calculation")