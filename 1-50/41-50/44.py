import time, itertools

def check(number): # n(3n - 1) / 2 = number => 3n ^ 2 - n - 2number = 0 => D = 1 + 24number => n = (1 +- sqrt(D)) / 6
    D = 1 + 24 * number
    if int(D ** 0.5) ** 2 != D:
        return False
    
    return (1 + int(D ** 0.5)) % 6 == 0


def main():
    min_d = 10 ** 18
    for j, k in itertools.product(range(1, 10001), repeat=2):
        p_j = j * (3 * j - 1) // 2
        p_k = k * (3 * k - 1) // 2

        if check(p_j + p_k) and check(abs(p_j - p_k)):
            min_d = min(min_d, abs(p_j - p_k))
    
    print(min_d)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")