def is_prime(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

# Example usage
number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
