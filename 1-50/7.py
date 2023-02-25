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
    count = 0
    number = 0

    while count < 10001:
        number += 1
        if prime(number):
            count += 1
    
    print(number)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")