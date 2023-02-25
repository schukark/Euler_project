import time

def name_score(name, index):
    total = 0

    for symbol in name:
        total += ord(symbol) - ord('A') + 1
    
    return (index + 1) * total

def main():
    f = open(r"1-50\21-30\p022_names.txt", 'r')
    mas = sorted([line[1:-1] for line in f.readline().split(',')])
    
    total = 0

    for index, name in enumerate(mas):
        total += name_score(name, index)
    
    print(total)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")