import time, itertools

def main():
    answer = set()

    for a, b in itertools.product(range(2, 101), repeat=2):
        answer.add(a ** b)
    
    print(len(answer))


if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")