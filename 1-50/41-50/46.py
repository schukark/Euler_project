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
    for i in range(33, 10000000, 2):
        if prime(i):
            continue

        d = 1
        while 2 * d * d <= i:
            if prime(i - 2 * d * d):
                break
            d += 1
        else:
            print(i)
            return None

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")