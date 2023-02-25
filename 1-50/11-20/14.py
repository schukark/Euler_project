import time

def main():
    longest_chain, best_num = 0, 0
    number = 1

    while number < 1_000_000:
        number_cpy = number
        count = 0

        while number_cpy != 1:
            if number_cpy % 2 == 0:
                number_cpy //= 2
            else:
                number_cpy = (3 * number_cpy + 1) // 2
                count += 1
            count += 1
        
        if longest_chain < count:
            longest_chain = count
            best_num = number
        number += 1
    
    print(longest_chain, best_num)


if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")