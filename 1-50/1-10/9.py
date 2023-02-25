import time

def main():
    for a in range(1, 1001):
        for b in range(1, 1001 - a):
            c = int((a ** 2 + b ** 2) ** 0.5)
            if c ** 2 == (a ** 2 + b ** 2) and a + b + c == 1000:
                print(a, b, c, a * b * c)
                return True

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")