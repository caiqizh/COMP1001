n = input('Please enter the combination of braces: ')
list = []
a = 'True'
for i in n:
    if i == '(' or i == '[' or i == '{':
        list.append(i)
    if i == ')':
        if list[len(list)-1] == '(':
            list = list[:len(list)-1]
        else:
            a = 'False'
    if i == ']':
        if list[len(list)-1] == '[':
            list = list[:len(list)-1]
        else:
            a = 'False'
    if i == '}':
        if list[len(list)-1] == '{':
            list = list[:len(list)-1]
        else:
            a = 'False'

if len(list) != 0:
    a = 'False'
print('The result is',a)
    
            
    
