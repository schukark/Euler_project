import time

def main():
    total_sum = 0

    for i in range(2, 1000000):
        sum_5 = sum([int(c) ** 5 for c in str(i)])
        
        if sum_5 == i:
            total_sum += i
    
    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")