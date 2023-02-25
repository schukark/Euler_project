import time, math

def main():
    n = 20
    print(math.factorial(2 * n) // math.factorial(n) ** 2)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")