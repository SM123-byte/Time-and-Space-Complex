seat_numbers = [101, 104, 108, 112, 115, 120, 125, 130, 135, 140, 145, 150]
target_seat = 130

print("=== MY TRAIN SEAT FINDER ===")
print(f"Available Seats (Sorted): {seat_numbers}")
print(f"Target Seat to Find: {target_seat}\n")

def iterative_binary_search(seats, target):
    low = 0 # first boundary
    high = len(seats) - 1

# while loop to find the exact position of the train seat
    while low <= high: 
        mid = (low + high) // 2 # Splits the data sets in two parts to allow searching  
        if seats[mid] == target:
            return mid
        elif target < seats[mid]:   # Shifts to see where train seat really is
            high = mid - 1
        else:
            low = mid + 1
    return -1 

def recursive_binary_search(seats, target, low, high):
    if low > high:
        return -1 
    mid = (low + high) // 2
    if seats[mid] == target:
        return mid
    elif target < seats[mid]:
        return recursive_binary_search(seats, target, low, mid - 1)
    else:
        return recursive_binary_search(seats, target, mid + 1, high)

iterative_result = iterative_binary_search(seat_numbers, target_seat)
recursive_result = recursive_binary_search(seat_numbers, target_seat, 0, len(seat_numbers) - 1)
# Tallies both the iteravattive and recursive results

print(f"Iterative Search Result: Found at index {iterative_result}")
print(f"Recursive Search Result: Found at index {recursive_result}\n") 