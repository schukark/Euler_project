import time

def sum_divisors(n):
    answer = 0

    d = 1
    while d * d <= n:
        if n % d == 0:
            answer += d + n // d - int(d * d == n) * d
        d += 1
    
    return answer - n

def main():
    total_sum = 0

    for i in range(1, 10001):
        if sum_divisors(i) != i and sum_divisors(sum_divisors(i)) == i:
            total_sum += i
    
    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")