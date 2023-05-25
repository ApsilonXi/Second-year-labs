#(a+b+c)*!
#(a+b+c)*cc

def NumbToWord(N, alf, n, simb):
    if N == 0:
        if simb == '!':
            print('!')
        elif simb == 'cc':
            print('cc')
    new = int(N/n)
    r = 1
    WORD = []
    while (r <= n) and (r >= 1):
        r = N - new*n
        if r == 0:
            new -= 1
            r = N - new*n
        if new <= 0:
            WORD.append((new, n, r))
            break
        WORD.append((new, n, r))
        N = new
        new = int(N/n)
    WORD.sort()
    S = ''
    for j in range(len(WORD)):  
        S += alf[WORD[j][2]-1]
    if simb == '!':
        print(S+'!')
    elif simb == 'cc':
        print(S+'cc')

Alf = ['a', 'b', 'c']
Regul = int(input("Количество цепочек: "))
Simb = input('Конечный символ: ')

for i in range(Regul+1):
    NumbToWord(i, Alf, len(Alf), Simb)    






    
    

    
