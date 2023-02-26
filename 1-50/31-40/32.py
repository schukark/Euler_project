import time

def check(n):
    d = 1
    while d * d <= n:
        digits = set()

        if n % d != 0:
            d += 1
            continue

        for i in str(d) + str(n // d) + str(n):
            digits.add(int(i))
        
        digits = sorted(digits)

        if digits == sorted(set([1, 2, 3, 4, 5, 6, 7, 8, 9])) and len(str(d) +  str(n // d) + str(n)) == 9:
            print(f"{d} * {n // d} = {n}")
            return True

        d += 1
    return False

def main():
    total_sum = 0
    for i in range(1, 100000):
        if check(i):
            total_sum += i
    
    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")