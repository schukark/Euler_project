import time

def main():
    print(sum([int(a) for a in str(2 ** 1000)]))

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")