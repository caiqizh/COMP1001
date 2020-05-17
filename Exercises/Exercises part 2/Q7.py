def main():
    inputV = input("Please enter a list of votes: ")
    listV = inputV.split()
    # count stores the number of votes of each candidate
    count = [0, 0, 0]
    for i in listV:
        count[int(i)-1] = count[int(i)-1] + 1
    printHistogram(count)
def printHistogram(count):
    if count[0]>count[1]:
        big = count[0]
    else:
        big = count[1]
    if count[2] > big:
        big = count[2]
    else:
        pass
    
    if count[0] < big:
        n1 = [' ']*(big-count[0]) + ['*']*count[0]
    if count[0] == big:
        n1 = ['*']*big

    if count[1] < big:
        n2 = [' ']*(big-count[1]) + ['*']*count[2]
    if count[1] == big:
        n2 = ['*']*big

    if count[2] < big:
        n3 = [' ']*(big-count[2]) + ['*']*count[2]
    if count[2] == big:
        n3 = ['*']*big
    
    for i in range(big):
        print(n1[i],n2[i],n3[i])
    print('1 2 3')

main()
        






    
main()
