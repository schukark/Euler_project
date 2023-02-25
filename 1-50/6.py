import time

def main():
    n = 100

    print(n ** 2 * (n + 1) ** 2 // 4 - n * (n + 1) * (2 * n + 1) // 6)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")