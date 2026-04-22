def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

number = 5
result = calculate_factorial(number)
print(f"--- Assignment 1 ---")
print(f"The factorial of {number} is: {result}")
