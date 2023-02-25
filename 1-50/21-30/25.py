import time

def main():
    a, b = 1, 2
    count = 3

    while True:
        if len(str(b)) >= 1000:
            print(count)
            return None
        a, b = b, a + b
        count += 1

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")