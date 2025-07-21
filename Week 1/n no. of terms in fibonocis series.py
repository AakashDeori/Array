// Input the number of terms from the user
n = int(input("Enter the number of terms for Fibonacci series: "))

# Initialize the first two terms of Fibonacci series
first = 0
second = 1

# Print the Fibonacci series
print("Fibonacci Series:")

# Special cases if user enters very small n
if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print(first)
else:
    print(first, second, end=" ")
    for i in range(2, n):
        next_term = first + second
        print(next_term, end=" ")
        first = second
        second = next_term
