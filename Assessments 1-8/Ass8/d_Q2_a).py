import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('GOOGL.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    k = 0
    for row in plots:
        if k == 0:
            k += 1
        else:
            x.append(int(k))
            y.append(eval(row[4]))
            k += 1

plt.plot(x,y, marker = 'x')
plt.xlabel('Days started from 11/13/2017 and end on 11/12/2018')
plt.ylabel('Stock price of GOOGL at closing')
plt.title('Stock price of GOOGL at closing for 11/13/2017-11/12/2018')
plt.show()

