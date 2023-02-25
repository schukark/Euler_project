import time

def modulo(a):
    while (a % 2 == 0 or a % 5 == 0) and a > 0:
        if a % 2 == 0:
            a //= 2
        if a % 5 == 0:
            a //= 5

    if 10 % a == 1:
        return 1
    
    count = 1
    current = 10

    while current > 1:
        count += 1
        current = (current * 10) % a

    if current == 0:
        return 0
    return count

def main():
    best, length = 1, 0

    for i in range(2, 1000):
        if modulo(i) > length:
            length = modulo(i)
            best = i
    
    print(best)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")