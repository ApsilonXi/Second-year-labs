def massive(A):
    kol = int(input('Введите кол-во элементов мн-ва: '))
    while kol != 0:
        A.add(input('Введите элемент мн-ва: '))
        kol -= 1
    return A

def printset(A):
    for i in A:
        print(i)
    print('Количество элементов в мн-ве: '+str(len(A)))

B = set()
printset(massive(B))

s1 = input('Введите первое предложение: ')
s2 = input('Введите второе предложение: ')
s1Word = s1.split(' ')
s2Word = s2.split(' ')
C = set()
D = set()
for i in s1Word:
    C.add(i)
for i in s2Word:
    D.add(i)

print('C <= D '+str(C.issubset(D)))
print('C >= D '+str(C.issuperset(D)))
print(C.symmetric_difference(D))

S = set(input('Введите слово: '))
rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'
eng = 'qwertyuiopasdfghjklzxcvbnm'
num = '1234567890'
setRu = set()
setEng = set()
setNum = set()
for i in S:
    if i in rus:
        setRu.add(i)
    elif i in eng:
        setEng.add(i)
    else:
        setNum.add(i)
print(setRu, '\n', setEng, '\n', setNum)
    

