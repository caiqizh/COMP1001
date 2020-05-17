def main():
    # get the file names
    infileName = input("What file stores the students' marks? ")
    outfileName = input("What file should the sorted data go to? ")

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    entireRecord = []
    firstLine = True
    # process each line of the input file except the first line
    for line in infile:
        if firstLine:
            firstLine = False
            firstLineText = line
        else:
            # converting the string into a list
            recordList = line.split(",")
            # sum the scores of the 10 assignments
            sum = 0
            for i in range(1,10):
                sum += int(recordList[i])
            # prepend enough 0 to the total score using zfill()
            # and then insert this new datum to the head of the list
            recordList.insert(0,str(sum).zfill(3))
            # append the resulting recordList to entireRecord
            entireRecord.append(recordList)

    # sort the list of lists in a nondecreasing order of the total score
    entireRecord.sort()
    # write the heading to the output file
    outfile.write("".join(firstLineText.split())+"\n")
    # convert the lists back to strings and write them to the output file
    for line in entireRecord:
        outfile.write(",".join(line[1:]))

    # close both files
    infile.close()
    outfile.close()

main()
