import matplotlib.pyplot as plt
import csv

x = []
y = []

def stockUp(priceFile):
    import matplotlib.pyplot as plt
    import csv
    x = []
    y = []

    with open(priceFile, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        k = 0
        for row in plots:
            if k == 0:
                k += 1
            else:
                x.append(int(k))
                y.append(eval(row[4]))
                k += 1

    upDays = [1]
    for i in range(1, len(y)):
        up = 1
        daysBefore = i - 1
        thisDay = i
        while daysBefore >= 0:
            if y[daysBefore] > y[thisDay]:
                upDays.append(up)
                break
            else:
                up += 1
                daysBefore -= 1
        else:
            upDays.append(thisDay + 1)

    print(upDays)
    print(y)
    
    plt.title('Stock price of GOOGL at closing for 11/13/2017-11/12/2018')
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Days started from 11/13/2017 and end on 11/12/2018')
    ax1.set_ylabel('Stock prices' )
    ax1.plot(x, y, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Up periods', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, upDays, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()



stockUp("GOOGL.csv")
