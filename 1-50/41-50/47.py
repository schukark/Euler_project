import time

def distinct_primes(n):
    d = 2
    result = set()
    while d * d <= n:
        while n % d == 0:
            result.add(d)
            n //= d
        d += 1
    
    if n > 1:
        result.add(n)
    
    return len(result)

def main():
    for i in range(15, 1000000):
        for j in range(4):
            if distinct_primes(i + j) != 4:
                break
        else:
            print(i)
            return None

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")