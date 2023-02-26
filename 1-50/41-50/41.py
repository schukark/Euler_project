import time

def generate(perm, mas, length):
    if len(perm) == length:
        mas += [perm]
        return None
    
    for x in range(1, length + 1):
        if str(x) not in perm:
            generate(perm + str(x), mas, length)

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
    max_prime = 0
    for i in range(1, 9):
        mas = []
        generate("", mas, i)

        for permutation in mas:
            if prime(int(permutation)):
                print(permutation, i)
                max_prime = max(max_prime, int(permutation))
    
    print(max_prime)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")