import time

def main():
    a, b = 1, 2
    total_sum = 0

    while b < 4_000_000:
        if (b % 2 == 0):
            total_sum += b
        a, b = b, a + b
    
    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")