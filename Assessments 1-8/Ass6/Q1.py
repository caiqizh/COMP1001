def main():

     # user inputs
     start, end = eval(input('Please enter a starting number and an ending number: '))
     column, space = eval(input("Please enter the number of numbers printed on a row and the number of spaces per item: "))

     # outputs
     print(40*"-")
     print("\nYour print-out of numbers {0:0}-{1:0} using {2:0} columns and {3:0} spaces between numbers:\n".format(start, end, column, space))
     for i in range(start, end+1):
          if (i-start) % column == 0:
               print()
          print("{0:>{width}}".format(i, width=space), end="")

main()
