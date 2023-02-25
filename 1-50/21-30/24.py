import time

def generate(current, mas):
    if len(current) == 10:
        mas.append(current)
        return None
    
    for i in range(10):
        if i not in current:
            generate(current + [i], mas)

def main():
    mas = []
    generate([], mas)

    mas.sort()

    print(''.join([str(el) for el in mas[999999]]))

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")