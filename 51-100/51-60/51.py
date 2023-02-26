import time, itertools

def prime(n):
    if n <= 1:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    
    return True

def count_primes(n):
    count = 0
    min_prime = 10 ** 18

    for digit in range(10):
        if n[0] == '*' and digit == 0:
            continue

        number = int(n.replace('*', str(digit)))

        if prime(number):
            count += 1
            min_prime = min(min_prime, number)

    
    return [count, min_prime]

def main():
    min_prime = 10 ** 18
    for count in range(1, 7):
        for array in itertools.product("*" + ''.join(map(str, list(range(10)))), repeat=count):
            if '*' not in array or array[0] == '0':
                continue

            result = count_primes(''.join(array)) 

            if result[0] == 8:
                min_prime = min(min_prime, result[1])
    
    print(min_prime)


if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")