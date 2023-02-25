import time

def main():
    total_sum = 0

    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    
    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")