import time, math

def main():
    mas = []
    for n in range(1, 101):
        for r in range(1, n + 1):
            c_n = math.factorial(n) // math.factorial(r) // math.factorial(n - r)
            mas += [c_n]
    print(len(list(filter(lambda x: x >= 10 ** 6, mas))))

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")