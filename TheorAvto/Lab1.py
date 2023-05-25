def menu():
    V = input('Выберите функцию:\n1. Найти по слову номер.\n2. Найти по номеру слово.\n')
    if V == '1':
        W = input('Введите слово, в котором содержаться буквы алфавита: ')
        for i in W:
            if i not in Alf:
                print('Одной или нескольких букв нет в алфавите.')
                menu()
        WordToNumb(W, Alf, n)
    elif V == '2':
        N = int(input('Введите номер слова: '))
        if N != 0:
            NumbToWord(N, Alf, n)
        else:
            print('Пустое слово')
    else:
        print('Такого варианта нет.')
        menu()

def WordToNumb(word, alf, n):
    k = len(word)
    N = 0
    sN = ''
    x = 1
    for i in word:    
        N += n**(k-x) * (alf.index(i)+1)
        sN += str(n)+'^'+str(k-x)+' * '+str(alf.index(i)+1)
        if x < k:
            sN += ' + '
        else:
            sN += ' = '+str(N)
        x += 1
    print(sN)

def NumbToWord(N, alf, n):
    new = int(N/n)
    SWord = ''
    r = 1
    WORD = []
    while (r <= n) and (r >= 1):
        r = N - new*n
        if r == 0:
            new -= 1
            r = N - new*n
        if new <= 0:
            break
        word = new*n + r
        WORD.append((new, n, r))
        N = new
        new = int(N/n)
    k = len(WORD)
    WORD.sort(reverse=False)
    print(WORD)
    S = ''
    SWord = str(WORD[0][1])+'^'+str(k)+' * '+str(WORD[0][0])+' + '
    t = 1
    for i in range(len(WORD)):
        SWord += str(WORD[i][1])+'^'+str(k-t)+' * '+str(WORD[i][2])+' + '
        t += 1
    S = alf[WORD[0][0]-1]
    for j in range(len(WORD)):  
        S += alf[WORD[j][2]-1]
    SWord = SWord[:-3]
    SWord += ' = ' + S
    print(SWord)

Alf = []
n = int(input('Введите количество символов в алфавите: '))
for i in range(n):
    Simb = input('Введите букву алфавита: ')
    while Simb in Alf:
        Simb = input('Введите другую букву алфавита: ')
    
    Alf.append(Simb)
#Alf.sort()
menu()


