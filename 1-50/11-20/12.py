import time

def divisors(n):
    result = 0

    d = 1
    while d * d <= n:
        result += int(n % d == 0) * 2 - int(d * d == n)
        d += 1
    
    return result

def main():
    for i in range(1, 100000000):
        number = i * (i + 1) // 2

        if divisors(number) > 500:
            print(number)
            return None

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")