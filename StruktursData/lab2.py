def replacement(F):
    with open('C:\EmilyVolkova\laba2TXT.txt', 'r+', encoding='utf-8') as f:
        row = int(input('Введите номер строки: '))
        if row > len(F):
            return print('Такой строки нет.\n--------------')
        col = int(input('Введите номер элемента: '))
        if col > len(F[row]):
            return print('Такого элемента нет.\n-------------')
        F[row] = F[row][:col] + input('Введите символ: ') + F[row][col:]
        for i in F:
            f.write(i)
        print('-----------------')

def Unic(D, F):
        unic = []
        for i in D:
            count2 = 0
            for j in F:
                l = j.split(' ')
                for q in l:
                    if (i == q) and (q != '\n'):
                        count2 += 1
            if count2 == 1:
                unic.append((i, count2))
        print(unic)

def Repeat(D, F):
        rep = []
        for i in D:
            count2 = 0
            for j in F:
                l = j.split(' ')
                for q in l:
                    if (i == q) and (q != '\n'):
                        count2 += 1
            if count2 > 1:
                rep.append((i, count2))
        print(rep)

#задание 1
with open('C:\EmilyVolkova\laba2NUM.txt', 'w') as f1:
    n = 0
    while n != '':
        n = input('Введите число: ')
        f1.write(n+' ')

with open('C:\EmilyVolkova\laba2NUM.txt', 'r') as f2:
    Nums = f2.readline().split(' ')
    c = 0
    for i in Nums:
        if (i != '') and (float(i) < 0):
            c += 1
    print('Количество отрицательных символов: '+str(c))

#задание 2
print('----------------')

with open('C:\EmilyVolkova\laba2TXT.txt', 'r', encoding='utf-8') as f2:
    F = f2.readlines()
    replacement(F)

    #задание 3
    row = int(input('Введите номер строки: '))
    if row > len(F)-1 :
        print('Такой строки нет.')
    else:
        print(F[row])
        #задание 4
        string = input('Введите подстроку: ')
        LIST = []
        Xed = 0
        for i in F:
            n = 0
            count1 = 0
            count1 = i.count(string)
            st = string.split(' ')
            if count1 != 0:
                LIST.append((F.index(i), i.find(st[0])+2))
        if len(LIST) == 0:
            print('Совпадений нет.')
        else:    
            print(LIST)
    

    #задание 5
    D = set()
    for i in F:
        for j in i.split(' '):
            if j != '\n':
                D.add(j)

    Unic(D, F)
    Repeat(D, F)


    


        
        





