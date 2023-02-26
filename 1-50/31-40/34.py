import time, math

def main():
    total_sum = 0
    for num in range(10, 100000):
        fact_sum = sum([math.factorial(int(i)) for i in str(num)])

        if fact_sum != num:
            continue

        print(f"{'! + '.join([i for i in str(num)])}! = {num}")
        total_sum += num
    
    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")