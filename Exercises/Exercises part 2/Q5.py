days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
# 0 represents Monday, 1 represents Tuesday and so on.
FIRST_DAY_JAN = 0; 

def main():

    m = int(input("Please enter a month (1 - 12) or -1 to end: "))

    while m != -1:

        # 0 represents Monday, 1 represents Tuesday and so on.
        startingDay = determine1stDayofMonth(m, days)       

        # print the calendar
        print("M   T   W   T   F   S   S")
        for i in range(startingDay):
            x = " "
            print("{0:<4}".format(x), end="")
        j = startingDay
        for i in range(1, days[m - 1] + 1):
            if j % 7 == 0 and i != 1:
                j = 0
                print()

            print("{0:<4}".format(i), end="")
            j = j + 1
        print()        
        m = int(input("Please enter a month (1 - 12) or -1 to end: "))
	
    print("Bye!");

def determine1stDayofMonth(m, days):
    day = 0
    for i in days[:m-1]:
        day = day + i
    k = day % 7
    startingDay = k
    
    return startingDay
    
        

main()

