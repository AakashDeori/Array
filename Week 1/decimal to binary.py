# Q3: Convert decimal to binary

# Input a decimal number from the user
decimal_number = int(input("Enter a decimal number: "))

# Convert decimal to binary using built-in function
binary_number = bin(decimal_number)[2:]  # [2:] to remove the '0b' prefix

# Display the binary equivalent
print(f"Binary equivalent of {decimal_number} is: {binary_number}")
