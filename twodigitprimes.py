primes = [
    num
    for num in range(10, 100) # CHecks the numbers from 10-100
       #Used all function - to check if all are true then it would print out in a list
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) # square root of num only needed
]