def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 29
result = is_prime(number)
print(f"--- Assignment 3 ---")
print(f"Is {number} a prime number? {result}")
