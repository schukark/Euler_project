import time

def main():
    for x in range(1, 10000000):
        mas = sorted([int(s) for s in str(x)])

        for count in range(2, 7):
            mas2 = sorted([int(s) for s in str(x * count)])
            if mas != mas2:
                break
        else:
            print(x)
            return None

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")