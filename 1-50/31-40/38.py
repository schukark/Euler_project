import time

def main():
    max_ans = 0
    for i in range(2, 100000):
        ans = ""
        count = 1

        while len(ans) < 9:
            ans += str(i * count)
            count += 1
        
        #print(i, ans)
        
        if len(ans) == 9 and len(set([i for i in ans])) == 9 and '0' not in ans:
            max_ans = max(max_ans, int(ans))
    
    print(max_ans)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")