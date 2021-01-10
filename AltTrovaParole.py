import numpy as np

# def lookAround(table, x, y, search, toFind):
#     l = []
#     print('x,y = ', x,y)
#     for i in range(-1,2):
#         for j in range(-1,2):
#             # print('cerco in posizione', x+i, y+j)
#             if x+i>=0 and y+j>=0:
#                 try:
#                     print('cercando l\'elemento ',table[x+i][y+j], ' in posizione ', [x+i],[y+j])
#                     if table[x+i][y+j]==toFind[search]:
#                         print('search', search)
#                         if search==len(toFind)-1:
#                             print('arrived', x, y)
#                             return x,y
#                         else:
#                             return lookAround(table, x+i, y+j, search+1, toFind)
#                 except:
#                     pass

def continueSearching(table, x, y, search, toFind, xDir, yDir):
    print('continue search',search)
    print(x+xDir, y+yDir)
    if x+xDir>=0 and y+yDir>=0:
        print('elif')
        try:
            if table[x+xDir][y+yDir]==toFind[search]:
                print('trovato in posizione ', x+xDir, y+yDir, 'in direzione ', xDir, yDir)
                
                if search==len(toFind)-1:
                    print('finito!')
                    return x+xDir, y+yDir
                else:
                    return continueSearching(table, x+xDir, y+yDir, search+1, toFind, xDir, yDir)
            else:
                return -1,-1
        except:
            pass
    else: return -1,-1

def lookAround(table, x, y, toFind, step):
    l = []
    print('-------------')
    print('xStart,yStart = ', x,y)
    for i in range(-1,2):
        for j in range(-1,2):
            if (i,j)==(0,0): pass
            step += 1
            print('looping i,j ',i,j)
            # print('cerco in posizione', x+i, y+j)
            if x+i>=0 and y+j>=0:
                try:
                    print('cercando l\'elemento ',table[x+i][y+j], ' in posizione ', [x+i],[y+j], 'SEARCH(', toFind[1],')')
                    if table[x+i][y+j]==toFind[1]:
                        if len(toFind)==2:
                            print('arrived, solo due passi, el.finale: ', x+i, y+j)
                            return x+i,y+j, step
                        else:
                            print('continuo')
                            xEnd, yEnd = continueSearching(table, x+i, y+j, 2, toFind, i, j)
                            if (xEnd,yEnd)!=(-1,-1):
                                print('lookAround return')
                                return xEnd, yEnd, step
                except:
                    pass

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
toFind = 'ab'


Letter = []
# print(len(table))
l = []
for i in range(len(table)):
    for el in range(len(table[i])):
        if table[i][el]==toFind[0]:
            Letter.append((i,el))
# Letter.append(l)

# l = len(Letter[0])
print(Letter)
print(Letter[0])
print('toFind[0]', toFind[0])
# print(table, Letter[i][0], Letter[i][1], 1, toFind)
# print(l)
# for j in range(len(toFind)-1):
#     l = len(Letter[j])
#     Letter.append([])
print('len toFind=',len(toFind))
for i in range(len(Letter)):
    # print(Letter[j][i][0], Letter[j][i][0])
    print('sto passando il ', i)
    x,y,step = lookAround(table, Letter[i][0], Letter[i][1], toFind,0)
    if (x,y)!=(-1,-1):
        print('APPOSTO', x,y)
    if step<10:
        x,y,step = lookAround(table, Letter[i][0], Letter[i][1], toFind,step)


print('trovati', x,y)
# print(Letter)

# for i i