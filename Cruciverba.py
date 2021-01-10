import numpy as np

def continueSearching(table, x, y, search, toFind, xDir, yDir):
    global foundWords
    if x+xDir>=0 and y+yDir>=0:
        try:
            if table[x+xDir][y+yDir]==toFind[search]:                
                if search==len(toFind)-1:
                    foundWords.append((x+xDir, y+yDir))
                else:
                    return continueSearching(table, x+xDir, y+yDir, search+1, toFind, xDir, yDir)
            else:
                pass
        except:
            pass
    else: pass

def lookAround(table, x, y, toFind):
    global foundWords
    for i in range(-1,2):
        for j in range(-1,2):
            if (i,j)==(0,0): pass
            if x+i>=0 and y+j>=0:
                try:
                    if table[x+i][y+j]==toFind[1]:
                        if len(toFind)==2:
                            foundWords.append((x+i,y+j))
                        else:
                            xEnd, yEnd = continueSearching(table, x+i, y+j, 2, toFind, i, j)
                            if (xEnd,yEnd)!=(-1,-1):
                                foundWords.append((xEnd, yEnd))
                except:
                    pass

def printWord(table, start, end, toFind):
    try:
        xDir = (end[0]-start[0])/abs(end[0]-start[0])
    except:
        xDir = 0
    try:
        yDir = (end[1]-start[1])/abs(end[1]-start[1])
    except:
        yDir = 0
    toBold = []
    toBold.append(start)
    for i in range(1,len(toFind)-1):
        toBold.append((int(start[0]+i*xDir), int(start[1]+i*yDir)))
    toBold.append(end)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if toBold[0]==(i,j):
                print(color.DARKCYAN + color.BOLD + table[i][j] + color.END + color.END, end=' ')
            elif toBold.count((i,j)): 
                print(color.RED + color.BOLD + table[i][j] + color.END + color.END, end=' ')
            else: 
                print(table[i][j],end=' ')
        print()
    print('-------------------')


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


table = []

# PER INSERIRE LA TABELLA
# while True:
#     nRow = 1
#     riga = input('riga: ')
#     # riga+=' '
#     if riga == '':
#         break
#     else:
#         # print(len(riga))
#         rowList = []
#         for i in range(len(riga)):
#             # print(i)
#             rowList.append(riga[i])
#         table.append(rowList)
#         # print(table)
# print(table)

# table = [
#     ['a','s','p','r','a','a'],
#     ['t','m','a','m','m','a'],
#     ['a','t','a','t','a','p'],
#     ['l','c','v','r','t','a'],
#     ['a','a','a','n','a','r'],
#     ]

table = [
    ['a','c','a','m','c','e','a','l','e','s','r','f','a','l','g'],
    ['c','n','a','l','s','m','a','t','r','i','m','o','n','i','o'],
    ['g','g','v','d','u','a','t','e','i','e','a','c','n','e','a'],
    ['f','m','m','s','r','r','o','s','s','r','n','f','i','k','n'],
    ['b','a','i','s','d','i','r','t','e','t','n','i','s','m','i'],
    ['a','c','n','v','y','t','i','i','l','m','o','a','l','d','s'],
    ['a','n','v','g','a','o','s','m','e','s','t','o','l','o','v'],
    ['m','f','i','e','t','t','a','o','a','s','t','d','m','g','i'],
    ['g','c','t','m','s','r','o','n','v','k','e','s','e','e','n'],
    ['l','d','a','l','e','e','m','e','o','c','a','r','l','m','o'],
    ['a','n','t','e','f','i','d','a','n','z','a','t','o','a','s'],
    ['s','o','i','b','i','d','f','i','g','e','w','i','l','g','e'],
    ['q','e','m','m','o','g','l','i','e','r','u','b','e','d','c'],
    ['a','a','d','e','d','i','l','e','f','e','s','s','v','e','u'],
    ['c','r','i','t','d','a','e','s','d','s','i','c','d','g','l'],
    ]
# VINO
# MATRIMONIO
# TESTIMONE
# MESTOLO
# LUCE
# MONETE
# MARITO
# ANNI
# VELO
# INVITATI
# MOGLIE
# MUSICA
# MAREE

while True:

    toFind = input('Che parola vuoi trovare?')
    if toFind == '': break
    # toFind = 'ab'

    Letter = []
    foundWords = []
    for i in range(len(table)):
        for el in range(len(table[i])):
            if table[i][el]==toFind[0]:
                Letter.append((i,el))
                lookAround(table, i, el, toFind)
                foundWords.append(0)

    #      0 1 2 3 4 5
    #    0 A S P R A A
    #    1 T M A M M A
    #    2 A T A T A P
    #    3 L C V R T A
    #    4 A A A N A R
    if np.all((np.asarray(foundWords,dtype=object) == 0)):
        print('Non ho trovato la parola')
    else:
        for i in range(len(foundWords)):
            if foundWords[i]!=0:
                countZero = np.count_nonzero(np.asarray(foundWords,dtype=object)[0:i]==0)
                printWord(table, Letter[countZero], foundWords[i], toFind)
