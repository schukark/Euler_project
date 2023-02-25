import time

def number_type(number):
    div_sum = 0
    d = 1

    while d * d <= number:
        if number % d == 0:
            div_sum += d + number // d - int(d * d == number) * d
        d += 1
    
    div_sum -= number

    if div_sum > number:
        return "abundant"
    elif div_sum < number:
        return "deficient"
    return "perfect"

def main():
    total = 0

    for i in range(1, 28124):
        flag = False
        for a in range(1, i):
            if number_type(a) == "abundant" and number_type(i - a) == "abundant":
                flag = True
                break
        
        if not flag:
            print(i)
            total += i
    
    print(f"Total is {total}")


if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")