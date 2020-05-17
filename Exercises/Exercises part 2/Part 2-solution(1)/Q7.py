def main():

    inputV = input("Please enter a list of votes: ")
    listV = inputV.split()

    count = [0, 0, 0]
    for i in listV:
        count[int(i)-1] = count[int(i)-1] + 1

    printHistogram(count)

def printHistogram(count):
    print("Here is the histogram:")
    maxNum = max(count);
    for i in range(int(maxNum), 0, -1):
        for j in range(3):
            if count[j] == i:
                print("{0:<3}".format("*"), end="")
                count[j] = count[j] - 1
            else:
                print("{0:<3}".format(" "), end="")
        print()
	
    for j in range(3):
        print("{0:<3}".format(str(j+1)), end="")
		
main()
