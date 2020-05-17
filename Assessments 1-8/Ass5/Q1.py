def reverseString(text):
     #text = input("\nPlease input a string: ")
          
     lst = text.split()
     # if there a full top at the end of the string
     if text[-1] == ".":
        # add a full stop to the end of the first word  
        lst[0] += "."
        # exclude the original full stop
        lst[-1] = lst[-1][0:-1]
     # join the items in the list from the end to the front
     newtext = " ".join(lst[::-1])
     return newtext

print("The correct output is:", reverseString("Here I am. Send me."))
print("The correct output is:", reverseString("Here I am. Send me!"))
print("The correct output is:", reverseString("All hard work brings a profit, but mere talk leads only to poverty."))
print("The correct output is:", reverseString("The beginning of wisdom is this: Get wisdom, and whatever you get, get insight."))

