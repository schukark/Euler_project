import time

def main():
    print(str(sum([i ** i for i in range(1, 1001)]))[-10:])

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")