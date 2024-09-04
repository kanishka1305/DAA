def is_prime(num, divisor=2):
    if num < 2:
        return False
    if divisor * divisor > num:
        return True
    if num % divisor == 0:
        return False
    return is_prime(num, divisor + 1)

def generate_primes(n, current=2):
    if current > n:
        return []
    if is_prime(current):
        return [current] + generate_primes(n, current + 1)
    return generate_primes(n, current + 1)

n = 100  
prime_numbers = generate_primes(n)
print(prime_numbers)
