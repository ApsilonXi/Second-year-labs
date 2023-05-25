import pandas as pd
    
def Tab(alf, indexes):
    tab = pd.DataFrame()
    for i in alf:
        for j in indexes:
            tab.loc[j, i] = 'NaN'
    return tab

def Print(graf, start, end, ind, n):
    if n == 0:
        START = []
        END = []
        for i in start:
            START.append(graf.index.values[int(i)])
            graf.index.values[int(i)] = '->'+graf.index.values[int(i)]
        for i in end:       
            END.append(graf.index.values[int(i)])
            graf.index.values[int(i)] = '<-'+graf.index.values[int(i)]
        print(graf)
        return graf, START, END
    else:
        graf.at["q0", "1"][0] = "q1"
        graf.at["q1", "0"][0] = "q2"
        graf.at["q1", "1"][0] = "q3"
        graf.at["q2", "0"][0] = "q3"
        graf.at["q2", "1"][0] = "q3"
        for i in range(len(ind)):
            if ind[i] in start:
                graf.index.values[i] = '->'+graf.index.values[i]
            if ind[i] in end:
                graf.index.values[i] = '<-'+graf.index.values[i]
        return graf


def TabZap(alf, indexes, start, end):
    n = 0
    grafFront = Tab(alf, indexes)
    grafBack = Tab(alf, indexes)
    for i in alf:
        for j in indexes:
            s = input('('+j+', '+i+') -> ')
            if (s == '-') or (s == ''):
                grafFront[i][j] = ['NaN']
                grafBack[i][j] = ['NaN']
            else:
                d = ''
                for q in range(0, len(s), 2):
                    d += s[q:q+2] + ' '
                D = d.split(' ')
                del D[len(D)-1]
                grafFront[i][j] = D 
                grafBack[i][j] = D 
    return grafBack, Print(grafFront, start, end, 0, 0)

def DeleteTops(graf, alf, indexes):
    for i in range(len(indexes)-1, 0, -1):
        ind = graf.index.values[i]
        n = 0
        for j in range(len(indexes)):
            if ind != indexes[j]:
                for p in range(len(alf)):
                    if ind in graf.loc[indexes[j], alf[p]]:
                        n += 1
        if n == 0:
            graf.drop(labels = ind, axis = 0, inplace = True)
            indexes.pop(int(ind[1]))
    return graf, indexes

def equivalence(graf, alf, equiv):
    LIST = []
    for i in range(len(alf)):
        SET = []
        for j in range(len(equiv)):
            poz = graf.loc[equiv[j], alf[i]]
            if poz[0] not in equiv:
                SET.append(equiv[j])
        if len(SET) != 0:
            LIST.append(SET)
    for i in range(len(LIST)):
        for j in range(len(LIST[i])):
            if LIST[i][j] in equiv:
                equiv.remove(LIST[i][j])
    return equiv, LIST

def TabEquivalence(graf, indexes, alf, equivs, ind, start, end):
    grafE = Tab(alf, ind)
    for i in range(len(equivs)):
        for j in range(len(alf)):
            if (len(equivs[i]) > 1):
                if (equivs[i][0] == "q4"):
                    grafE.at["q3", alf[j]] = ["q3"]
                else:
                    grafE.at[equivs[i][0], alf[j]] = [equivs[i][0]]
            else:
                grafE.at[equivs[i][0], alf[j]] = graf.loc[equivs[i], alf[j]][0]
    return Print(grafE, start, end, ind, -1)


Alf = []
n = int(input('Введите количество символов в алфавите: '))
for i in range(n):
    Simb = input('Введите букву алфавита: ')
    while Simb in Alf:
        Simb = input('Введите другую букву алфавита: ')
    Alf.append(Simb)

Kv = int(input("Кол-во вершин: "))
start = input("Введите номер начальной вершины: ").split(', ')
end = input("Введите номер конечной вершины: ").split(', ')
sq = ['q'+str(i) for i in range(Kv)]

GrafBack, [GrafFront, Start, End] = TabZap(Alf, sq, start, end)
GrafBack_2, new_sq = DeleteTops(GrafBack, Alf, sq)

for i in range(len(End)-1):
    if End[i] not in new_sq:
        End.pop(i)

equiv_0 = []
equiv_k = []
for i in range(len(new_sq)):
    if new_sq[i] in End:
        equiv_k.append(new_sq[i])
    else:
        equiv_0.append(new_sq[i])

final = []
FINAL = []
equiv1, LIST = equivalence(GrafBack_2, Alf, equiv_k)
if len(LIST) == 0:
    final.append(equiv1)
else:
    for i in range(len(LIST)):
        final.append(LIST[i])
    n = 0
    while n != 0:
        equiv1, LIST = equivalence(GrafBack_2, Alf, equiv1)
        n += 1
        for i in range(len(LIST)):
            final.append(LIST[i])

equiv2, LIST = equivalence(GrafBack_2, Alf, equiv_0)
if len(LIST) == 0:
    final.append(equiv2)
else:
    for i in range(len(LIST)):
        final.append(LIST[i])
    n = 0
    while n != 10:
        equiv2, LIST = equivalence(GrafBack_2, Alf, equiv2)
        n += 1
        for i in range(len(LIST)):
            final.append(LIST[i])

for i in range(len(final)):
    p = final[i]
    FINAL.append(list(p))
if FINAL[len(FINAL)-1][0] in FINAL[len(FINAL)-2]:
    FINAL[len(FINAL)-2].remove(FINAL[len(FINAL)-1][0])      
new_f = sorted(FINAL)
new_f.pop(0)
new_f[1].pop(1)

equivs_sq = []
nSTART = []
nEND = []
for i in range(len(new_f)): 
    if new_f[i][0] in Start:
        nSTART.append(new_f[i][0])
    elif new_f[i][0] in End:
        if new_f[i][0] == "q4":
            nEND.append("q3")
    if len(new_f) == 1:
        equivs_sq.append(new_f[i][0])
    else:
        equivs_sq.append(new_f[i][0])      

new_ind = sorted(equivs_sq)
new_ind[len(new_ind)-1] = "q3"

GrafBack_3 = TabEquivalence(GrafBack_2, sq, Alf, new_f, new_ind, nSTART, nEND)
print(GrafBack_3)

