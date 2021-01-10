import numpy as np

def lookAround(table, x, y, search):
    l = []
    print('x,y = ', x,y)
    for i in range(-1,2):
        for j in range(-1,2):
            print('cerco in posizione', x+i, y+j)
            if x+i>=0 and y+j>=0:
                try:
                    print('cercando l\'elemento ',table[x+i][y+j], ' in posizione ', [x+i],[y+j])
                    if table[x+i][y+j]==search:
                        l.append((x+i,y+j))
                        print('trovato')
                except:
                    pass
    print('l: ',l)
    return l

table = []
ok = True

# while True:
#     nRow = 1
#     riga = input()
#     # riga+=' '
#     if riga == '':
#         break
#     else:
#         print(len(riga))
#         rowList = []
#         for i in range(len(riga)):
#             print(i)
#             rowList.append(riga[i])
#         table.append(rowList)
#         print(table)

table = [['a','b','c'],['a','b','c']]

# table = np.array(table)
print(table)
# toFind = input('Che parola vuoi trovare?')
toFind = 'abc'


Letter = []
# print(len(table))
l = []
for i in range(len(table)):
    for el in range(len(table[i])):
        if table[i][el]==toFind[0]:
            l.append((i,el))
            Letter.append(lookAround(table, i, el, toFind[j+1]))


Letter.append(l)

# l = len(Letter[0])
print(Letter)
print(l)
# for j in range(len(toFind)-1):
#     l = len(Letter[j])
#     Letter.append([])
#     for i in range(l):
#         print(Letter[j][i][0], Letter[j][i][0])
#         # Letter.append(lookAround(table, Letter[j][i][0], Letter[j][i][1], toFind[j+1]))

print(Letter)

# for i i