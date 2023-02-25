import time

def main():
    num = 600851475143

    max_prime = 0

    d = 2
    while d * d <= num:
        while num % d == 0:
            max_prime = max(max_prime, d)
            num //= d
        d += 1
    
    max_prime = max(max_prime, num)

    print(max_prime)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")