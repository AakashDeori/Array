# Q2: Program to count the no. of positive & sequence no.

# Input: Number of elements to be stored in the array
n = int(input("Enter how many numbers you want to input: "))

# Create an empty list (array)
arr = []

# Input the elements one-by-one and store them in the list
for i in range(n):
    element = int(input(f"Enter number {i+1}: "))
    arr.append(element)

# Initialize counters for positive numbers and sequence numbers
positive_count = 0
sequence_count = 0

# Count how many numbers are positive (> 0)
for num in arr:
    if num > 0:
        positive_count += 1

# Count how many numbers are in increasing sequence from the previous one
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        sequence_count += 1

# Display the results
print("\nTotal Positive Numbers:", positive_count)
print("Total Sequence Numbers (increasing from previous):", sequence_count)
