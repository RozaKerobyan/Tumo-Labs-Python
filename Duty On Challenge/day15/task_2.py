def is_prime(n):
    # Check if a number is prime
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    # Find all prime numbers in a given range
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

primes = find_primes_in_range(0, 100)
# Result
print(primes)
