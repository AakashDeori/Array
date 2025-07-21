# Q1: Program to input elements of array and print all the elements

# Input the number of elements
n = int(input("Enter the number of elements: "))

# Initialize an empty list
arr = []

# Input elements into the list
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    arr.append(element)

# Print all elements
print("\nThe elements of the array are:")
for item in arr:
    print(item)


