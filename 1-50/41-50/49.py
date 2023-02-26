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
    for center in range(1001, 10000):
        if not prime(center):
            continue
        second = sorted([int(i) for i in str(center)])

        for delta in range(1, min(center, 10000 - center)):
            if not prime(center - delta) or not prime(center + delta):
                continue
                
            first = sorted([int(i) for i in str(center - delta)])
            last = sorted([int(i) for i in str(center + delta)])

            if first != second or second != last or first != last:
                continue

            print(center - delta, center, center + delta)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")