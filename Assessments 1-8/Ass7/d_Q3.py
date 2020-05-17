def allpeople():
    allpeople = []
    for i in range(170):
        allpeople.append(i)
    return allpeople

import random

def creatLinks():
    all = allpeople()
    couple = random.sample(all,2)

    return couple #couple is a list.

def genGraph():
    listfriends = [] #listfriends is a list.
    print('first step done')

    while len(listfriends) < 800:
        couple = creatLinks()
        if not (couple in listfriends or couple[::-1] in listfriends) :
            listfriends.append(couple)
    friends = {}

    for i in range(170):
        values = set()
        for j in listfriends:
            if i == j[0]:
                values.add(j[1])
            if i == j[1]:
                values.add(j[0])
        friends[i] = values
    return friends

def mostPopular(dict):
    list = []
    big = set('')
    for i in dict:
        if len(dict[i]) > len(big):
            big = dict[i]
    for i in dict:
        if len(dict[i]) == len(big):
            list.append(str(i))
    return list



allPeople = set(allpeople())
friends = genGraph()

# allPeople is a set of all people.
# friends is a dictionary for the friendship.
size = 0

for person in allPeople:
    print(str(person)+":", friends[person])
    size += len(friends[person])

mostPopular = mostPopular(friends)
k = int(mostPopular[0])

number = len(friends[k])
print(size)


print()
print('The number of directional friendship links is:', size)
print('The most popular person is/are',','.join(mostPopular)+'.')
print('They/she/he has',number,'friends.')
