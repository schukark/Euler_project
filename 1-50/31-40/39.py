import time

def count_solutions(p):
    count = 0
    for a in range(1, p):
        for b in range(a, p - a):
            c = p - a - b

            if c ** 2 == a ** 2 + b ** 2:
                count += 1
    
    return count

def main():
    max_count, perim = 0, 0

    for p in range(1000):
        if count_solutions(p) > max_count:
            max_count = count_solutions(p)
            perim = p
    
    print(max_count, perim)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")