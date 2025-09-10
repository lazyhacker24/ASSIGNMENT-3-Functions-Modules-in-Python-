# Function to calculate factorial
# pardeep
def factorial(n):
    if n == 0 or n == 1:   
        return 1
    else:
        return n * factorial(n - 1)   

# Taking input from user
num = int(input("Enter a number: "))

# Calling the function and printing result
print(f"The factorial of {num} is: {factorial(num)}")
