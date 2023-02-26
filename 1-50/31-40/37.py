import time

def prime(n):
    if n == 0:
        return True

    if n % 2 == 0 or n < 2:
        return n == 2

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    
    return True

def main():
    total_sum = 0
    for i in range(10, 1000000):
        for shift in range(len(str(i))):
            left_num = str(i)[shift:]
            right_num = str(i)[:shift]

            if left_num == '':
                left_num = 0
            else:
                left_num = int(left_num)
            
            if right_num == '':
                right_num = 0
            else:
                right_num = int(right_num)
            
            if not prime(left_num) or not prime(right_num):
                break
        else:
            print(i)
            total_sum += i

    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")