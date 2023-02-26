import time, itertools, math, functools

def main():
    result = []
    for a, b in itertools.product(range(11, 100), repeat=2):
        if a % 10 == 0 or b % 10 == 0 or a >= b:
            continue

        a_1, a_2 = a // 10, a % 10
        b_1, b_2 = b // 10, b % 10

        if a_1 == b_1 and b_2 * a == a_2 * b:
            print(f"{a} / {b} = {a_1} / {b_1}")
            result += [[a_1, b_1]]

        if a_1 == b_2 and b_1 * a == a_2 * b:
            print(f"{a} / {b} = {a_1} / {b_2}")
            result += [[a_1, b_2]]

        if a_2 == b_2 and b_1 * a == a_1 * b:
            print(f"{a} / {b} = {a_2} / {b_2}")
            result += [[a_2, b_2]]

        if a_2 == b_1 and b_2 * a == a_1 * b:
            print(f"{a} / {b} = {a_1} / {b_2}")
            result += [[a_1, b_2]]
    
    denom_1 = functools.reduce(lambda x, y: x * y, [denom for num, denom in result])
    num_1 = functools.reduce(lambda x, y: x * y, [num for num, denom in result])

    print(f"{num_1 // math.gcd(num_1, denom_1)} / {denom_1 // math.gcd(num_1, denom_1)}")

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")