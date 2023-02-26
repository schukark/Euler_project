import time

def main():
    f = open(r"1-50\41-50\p042_words.txt", 'r')

    count = 0

    word_list = [word[1:-1] for word in f.readline().split(',')]
    
    for word in word_list:
        letter_sum = sum([ord(letter) - ord('A') + 1 for letter in word])

        d = 1  + 8 * letter_sum #n ^ 2 + n = 2 * letter_sum => d = 1 + 8 * letter_sum => n = (-1 +- sqrt(d)) / 2

        if int(d ** 0.5) ** 2 != d:
            continue

        if int(d ** 0.5) % 2 != 1:
            continue
        
        count += 1
    
    print(count)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")