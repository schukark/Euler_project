import time

def prime(n):
    if n <= 1:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    
    return True

def main():
    primes = [2]

    count = 0
    number = 3
    max_count = 0
    max_prime = 0

    while count < 1000:
        if prime(number):
            primes += [number + primes[-1]]
            count += 1
        number += 1
    
    for start in range(1, len(primes)):
        for count in range(1, len(primes) - start):
            cumulative = primes[start + count - 1] - primes[start - 1]
            if not prime(cumulative) or cumulative >= 1000000:
                continue
            
            if max_count < count:
                max_count = count
                max_prime = cumulative
    
    print(max_count, max_prime)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")