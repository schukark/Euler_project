import time

def prime(n):
    if n % 2 == 0 or n < 2:
        return n == 2
    
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    
    return True

def main():
    total_sum = 0
    current = 1

    while current < 2_000_000:
        if prime(current):
            total_sum += current
        current += 1
    
    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")