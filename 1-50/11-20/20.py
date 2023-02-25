import time, math

def main():
    print(sum([int(i) for i in str(math.factorial(100))]))

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")