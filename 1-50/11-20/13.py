import time

def main():
    f = open(r'1-50\11-20\13.txt', 'r')

    print(str(sum([int(s) for s in f.readlines()]))[:10])

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")