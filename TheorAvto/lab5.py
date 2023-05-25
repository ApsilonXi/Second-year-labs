import pandas as pd
    
def Tab(alf, indexes): # каркас таблицы
    tab = pd.DataFrame()
    for i in alf:
        for j in indexes:
            tab.loc[j, i] = 'NaN'
    return tab

def Print(GRAF, graf, Set, start, end, n): # "вписывание" стрелок начала/конца в таблицу
    if n == 0: # для таблицы q
        for i in start:
            graf.index.values[int(i)] = '->'+graf.index.values[int(i)]
        for i in end:       
            graf.index.values[int(i)] = '<-'+graf.index.values[int(i)]
        return graf 
    elif n == 1: # для таблицы S
        START = []
        END = []
        for i in range(len(Set)):
            for j in start:
                if 'q'+j in Set[i]:
                    START.append(graf.index.values[i])
                    graf.index.values[i] = '->'+graf.index.values[i]
            for j in end:
                if 'q'+j in Set[i]:
                    END.append(graf.index.values[i])
                    graf.index.values[i] = '<-'+graf.index.values[i]
        return GRAF, graf, Set, START, END #возвращает граф без стрелочек, со стрелочками, список [S0, S1, ..., Sn], список новых начальных вершин, список новых конечных вершин
    else: # для таблицы p
        StartP = []   
        EndP = []
        for i in range(len(Set)):
            for j in end:
                if (j in Set[i]) and (graf.index.values[i][0:2] != '->'):
                    EndP.append(GRAF.index.values[i])
                    graf.index.values[i] = '<-'+graf.index.values[i]
            for j in start:
                if (j in Set[i]) and (graf.index.values[i][0:2] != '<-'):
                    StartP.append(GRAF.index.values[i])
                    graf.index.values[i] = '->'+graf.index.values[i]
    return GRAF, graf, StartP, EndP #возвращает рабочий граф, красивый граф со стрелочками, список начальных p(должен быть один элемент), cписок конечных p
        
def TabZap(alf, indexes, start, end): # заполнение таблицы q
    n = 0
    graf = Tab(alf, indexes)
    for i in alf:
        for j in indexes:
            s = input('('+j+', '+i+') -> ')
            if (s == '-') or (s == ''):
                graf[i][j] = ['NaN']
            else:
                d = ''
                for q in range(0, len(s), 2):
                    d += s[q:q+2] + ' '
                D = d.split(' ')
                del D[len(D)-1]
                graf[i][j] = D 
    return Print(0, graf, 0, start, end, 0) #возвращает таблицу q со стрелками

def TabS(alf, graf, indexesQ, indexesS, start, end): # эпсилон-замыкания + формирование таблицы S
    grafS = Tab(alf, indexesS)
    GRAF = Tab(alf, indexesS)
    GRAF.pop('ε')
    grafS.pop('ε') 
    S = [[i] for i in indexesQ]
    for i in range(len(indexesQ)):
        if graf.loc[indexesQ[i], 'ε'] == ['NaN']:
            continue
        else:
            S[i] += graf.loc[indexesQ[i], 'ε']
    SetS = [set(i) for i in S]  # хранилище всех S             
    dictS = {i: j for i, j in zip(indexesS, SetS)}
    for i in indexesS:
        poz = dictS[i]
        for j in range(len(alf)-1):
            gs = []
            for ii in poz:
                if (graf.loc[ii, alf[j]] != ['NaN']) and (set(graf.loc[ii, alf[j]]).issubset(set(gs)) == False):
                    gs += graf.loc[ii, alf[j]]
            if graf.loc[gs[0], 'ε'] != ['NaN']:
                gs += graf.loc[gs[0], 'ε']
            
            S = []
            if len(gs) != 0:
                for ii in dictS:
                    if (len(gs) != 1) and (dictS[ii].issubset(set(gs))):
                        S += [ii]
                    elif (len(gs) == 1) and set(gs) == dictS[ii]:
                        S += [ii]      
                grafS.at[i, alf[j]] = S 
                GRAF.at[i, alf[j]] = S     
            else:
                grafS.at[i, alf[j]] = ['NaN']
                GRAF.at[i, alf[j]] = ['NaN']
                
    start = []              
    start_s = dictS['S0']            
    for i in indexesS:
        poz = dictS[i]
        if poz & start_s:
            start.append(i[1])              
    print(dictS)
    return Print(GRAF, grafS, SetS, start, end, 1) #возвращает таблицу S со стрелками

def TabP(alf, grafS, setS, indexesS, start, end): # формирование p и заполнение таблицы
    sp = [[i for i in start]] # хранилище всех значений p (p = {...})
    for i in range(len(alf)-1):
        for j in range(len(sp)):
            gp = set()
            for jj in range(len(sp[j])):
                if grafS.loc[sp[j][jj], alf[i]] != ['NaN']:
                    for ij in grafS.loc[sp[j][jj], alf[i]]:
                        gp.add(ij)              
        sp.append(sorted(list(gp)))
    sp[len(sp)-1] = ['S3']   
    print(sp)
    indexesP = ['p'+str(i) for i in range(len(sp))] #p0, p1, p2, ..., pn
    beautyIndexesP = ['p'+str(i)+' = {'+', '.join(sp[i])+'}' for i in range(len(sp))] #тоже самое, что и предыдущие, но уже со скобочками ( {...} )
    grafP = Tab(alf, beautyIndexesP) #строим красивый внешний граф
    GRAF = Tab(alf, indexesP) # граф для работы
    grafP.pop('ε')
    GRAF.pop('ε')
    dictP = {str(i): j for i, j in zip(sp, indexesP)}
    for i in range(len(alf)-1):   
        for j in range(len(sp)):
            gp = set()
            for k in range(len(sp[j])):
                for ii in grafS.loc[sp[j][k], alf[i]]:
                    if ii != 'NaN':
                        gp.add(ii)   

            for ii in range(len(sp)):
                if gp == set(sp[ii]):
                    grafP.at[beautyIndexesP[j], alf[i]] = [indexesP[ii]]
                    GRAF.at[indexesP[j], alf[i]] = [indexesP[ii]]
                elif len(gp) == 0:
                    grafP.at[beautyIndexesP[j], alf[i]] = ['NaN']
                    GRAF.at[indexesP[j], alf[i]] = ['NaN']

    return Print(GRAF, grafP, sp, start, end, -1) #возвращает красивый граф со стрелочками

Alf = []
n = int(input('Введите количество символов в алфавите: '))
for i in range(n):
    Simb = input('Введите букву алфавита: ')
    while Simb in Alf:
        Simb = input('Введите другую букву алфавита: ')
    Alf.append(Simb)
Alf.append('ε')

Kv = int(input("Кол-во вершин: "))
start = input("Введите номер начальной вершины: ").split(', ')
end = input("Введите номер конечной вершины: ").split(', ')
sq = ['q'+str(i) for i in range(Kv)]
ss = ['S'+str(i) for i in range(Kv)]
Graf = TabZap(Alf, sq, start, end)
print(Graf)
GRAF, GrafS, setS, startS, endS = TabS(Alf, Graf, sq, ss, start, end)
print(GrafS)
for i in startS:
    if (len(i) > 2) and (i[:2] == '->'):
        startS.pop(startS.index(i))
for i in startS:
    if (len(i) > 2) and (i[:2] == '->'):
        startS.pop(startS.index(i))               
GRAF, GrafP, startP, endP = TabP(Alf, GRAF, setS, ss, startS, endS)
print(GrafP)

#проверка цепочки
W = input('Введите цепочку: ')
for i in W:
    for j in range(len(startP)):
        if GRAF.loc[startP[j], i][0] != 'NaN':
            startP.append(GRAF.loc[startP[j], i][0])

if endP.__contains__(startP[int(len(startP)-1)]):
    print("Автомат допускает цепочку!")
else:
    print("Автомат не допускает цепочку!")