import time
import itertools

def main():
    max_num = 0
    for a, b in itertools.product(range(100, 1000), repeat=2):
        new_num = a * b
        if new_num == int(str(new_num)[::-1]):
            max_num = max(max_num, new_num)
    
    print(max_num)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")