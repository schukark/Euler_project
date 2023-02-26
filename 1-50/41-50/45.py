import time

def check_hex(number): #n(2n - 1) = number => 2n ^ 2 - n = number => D = 1 + 8number => n = (1 + sqrt(D)) / 4
    D = 1 + 8 * number
    if int(D ** 0.5) ** 2 != D:
        return False
    
    return (1 + int(D ** 0.5)) % 4 == 0

def check_penta(number): # n(3n - 1) / 2 = number => 3n ^ 2 - n - 2number = 0 => D = 1 + 24number => n = (1 +- sqrt(D)) / 6
    D = 1 + 24 * number
    if int(D ** 0.5) ** 2 != D:
        return False
    
    return (1 + int(D ** 0.5)) % 6 == 0


def main():
    for n in range(286, 100000):
        tri = n * (n + 1) // 2

        if not check_penta(tri):
            continue

        if not check_hex(tri):
            continue

        print(n, tri)
        return None


if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")