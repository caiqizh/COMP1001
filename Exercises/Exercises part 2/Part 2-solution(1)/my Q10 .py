import csv
infile = open('student_record.csv', 'r')
data = infile.readlines()
del data[0]
ids = []
for row in data:
    row = row.split()
    id = row[1].split(',')[1]
    ids.append(id)
i = 7

while True:
    idss = []
    for k in ids:
        k = k[i:]
        idss.append(k)
    if len(set(idss)) == len(idss):
        for j in idss:
            print(j)
        break    
    else:
        i -= 1
    
    
