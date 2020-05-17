def main():
    a, b = eval(input('Pleas enter a starting number and an ending number: '))
    print('Please enter the number of numbers printed on a row')
    c, d = eval(input('and the number of spaces per item: '))
    print('----------------------------------------')
    print()
    print('Your print-out of numbers ' + str(a) + '-' + str(b) + ' using ' + str(c) +'columns')
    print('and ' + str(d) + ' spaces between numbers:')
    print()
    width = d
    while a <= b:
        list = []
        for i in range(0,c):
            A ='{0:<{width}}'.format(a, width = d)
            list = list + [A]
            a = a + 1
            if a > b:
                break
        print(''.join(list))
main()
