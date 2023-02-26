import time, functools

def main():
    s = ''.join([str(i) for i in range(1, 1000000)])

    print(functools.reduce(lambda x, y: x * y, [int(s[10 ** i - 1]) for i in range(0, 6 + 1)]))

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")