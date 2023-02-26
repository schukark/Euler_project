import time

def prime(n):
    if n % 2 == 0 or n < 2:
        return n == 2

    d = 3

    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    
    return True

def main():
    count = 0
    for i in range(2, 10 ** 6):
        flag = True

        if  not prime(i):
            continue

        for shift in range(len(str(i))):
            new_num = int(str(i)[shift:] + str(i)[:shift])
            if not prime(new_num):
                flag = False
                break
        
        if flag:
            count += 1
    
    print(count)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")