import time

def main():
    size = 1001
    mas = [[0 for i in range(size)] for j in range(size)]

    cur_x = 0
    cur_y = size - 1
    direction = 2 #0 -> right, 1-> down, 2 -> left, 3 -> up
    cur_num = size ** 2

    mas[cur_x][cur_y] = cur_num
    cur_num -= 1

    while cur_num > 1:
        new_x = cur_x
        new_y = cur_y

        if direction == 0:
            new_y += 1
        if direction == 1:
            new_x += 1
        if direction == 2:
            new_y -= 1
        if direction == 3:
            new_x -= 1
        
        if new_x >= size or new_y >= size or new_x < 0 or new_y < 0:
            direction = (direction + 3) % 4
            continue
            
        if mas[new_x][new_y] != 0:
            direction = (direction + 3) % 4
            continue
        
        mas[new_x][new_y] = cur_num
        cur_num -= 1

        cur_x, cur_y = new_x, new_y
    
    mas[size // 2][size // 2] = 1
    
    #print(*mas, sep='\n')

    total_sum = 0

    for i in range(size):
        total_sum += mas[i][i]
        total_sum += mas[i][size - i - 1]
    
    total_sum -= mas[size // 2][size // 2]

    print(total_sum)

if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")