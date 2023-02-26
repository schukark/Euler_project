import time

def main():
    total_sum = 0

    for i in range(1, 10 ** 6):
        if str(i) != str(i)[::-1]:
            continue

        if str(bin(i))[2:] != (str(bin(i))[2:])[::-1]:
            continue

        total_sum += i
    
    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")