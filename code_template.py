import time

def main():
    print("doing something...")

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")