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
    max_count = 0
    best_a, best_b = 0, 0

    for a in range(-1000 + 1, 1000):
        for b in range(-1000, 1001):
            count = 0

            while True:
                if prime(count ** 2 + a * count + b):
                    count += 1
                else:
                    break
            
            if count > max_count:
                max_count = count
                best_a = a
                best_b = b
    
    print(best_a * best_b)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")