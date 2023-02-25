import time

def leap_check(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    return n % 4 == 0

def main():
    day, week_day, month, year = 0, 0, 0, 1900
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    sunday_count = 0

    while year <= 2000:
        if week_day == 6 and day == 0 and year >= 1901:
            sunday_count += 1
        
        day += 1
        week_day += 1

        if week_day >= 7:
            week_day = 0
        
        if day >= months[month]:
            day = 0
            month += 1
        
        if month >= 12:
            month = 0
            year += 1
        
        months[1] = 28 + int(leap_check(year))
    
    print(sunday_count)



if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()

    print(f"Done in {end - start} seconds")