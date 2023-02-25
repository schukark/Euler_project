import time

def main():
    letter_count = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
                    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
                    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    
    decades_count = {0: "", 2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty",
                    7: "seventy", 8: "eighty", 9: "ninety"}
    
    string = []

    for i in range(1, 1000):
        a, b, c = i // 100, (i // 10) % 10, i % 10

        word = ""

        if a > 0:
            word += letter_count[a] + "hundred" + "and" * (b * b + c * c > 0)
        if b == 1:
            word += letter_count[10 + c]
        else:
            word += decades_count[b] + letter_count[c]
        
        string += [word]

    
    #print(string)
    print(sum([len(s) for s in string]) + len("onethousand"))


if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")