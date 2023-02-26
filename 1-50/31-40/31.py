import time

def main():
    count = 0
    for i_200 in range(2):
        for i_100 in range((200 - i_200 * 200) // 100 + 1):
            for i_50 in range((200 - i_200 * 200 - 100 * i_100) // 50 + 1):
                for i_20 in range((200 - i_200 * 200 - 100 * i_100 - 50 * i_50) // 20 + 1):
                    for i_10 in range((200 - i_200 * 200 - 100 * i_100 - 50 * i_50 - 20 * i_20) // 10 + 1):
                        for i_5 in range((200 - i_200 * 200  - 100 * i_100 - 50 * i_50 - 20 * i_20 - 10 * i_10) // 5 + 1):
                            remainder = 200 - 200 * i_200 - 100 * i_100 - 50 * i_50 - 20 * i_20 - 10 * i_10 - 5 * i_5
                            count += remainder // 2 + 1
        
    print(count)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")