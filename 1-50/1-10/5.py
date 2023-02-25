import time
import math

def main():
    lcm = 1

    for i in range(1, 21):
        lcm = lcm * i // math.gcd(lcm, i)
    
    print(lcm)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")