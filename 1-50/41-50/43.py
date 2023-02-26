import time

def generate(perm, mas):
    if len(perm) == 10:
        mas += [perm]
        return None
    
    for x in range(10):
        if str(x) not in perm:
            generate(perm + str(x), mas)

def main():
    mas = []
    total_sum = 0
    generate("", mas)

    primes = [2, 3, 5, 7, 11, 13, 17]

    for perm in mas:
        for shift in range(1, 8):
            number = int(perm[shift: shift + 3])

            if number % primes[shift - 1] != 0:
                break
        else:
            total_sum += int(perm)
    
    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")