def thirdtype(N, head, tail):
    for i in head:
        if len(i) > 1:
            return False
    left = 0
    right = 0
    for i in tail:
        if (sum(map(str.isupper, i)) == 1) or (sum(map(str.isupper, i)) == 0):
            for j in N:
                if i.find(j) == 0:
                    left += 1
                elif i.find(j) == len(i)-1:
                    right += 1
        else:
            return False
    if left == 0:
        print("Тип 3: праволинейная")
    elif right == 0:
        print("Тип 3: леволинейная")

def secondtype(head):
    for i in head:
        if (len(i) > 1) or (sum(map(str.isupper, i)) > 1):
            return False
    return True

def firsttype(head, tail):
    f, s = 0, 0
    ks1, ks2 = "", ""
    for i in range(len(head)):
        if len(head[i]) <= len(tail[i]):
            f += 1
        if len(head[i]) == 1:
            s += 1
        else:
            if len(head[i]) == 1:
                s += 1
                continue
            if len(head[i]) % 2 == 0:
                ks1 = head[i][:len(head[i]) // 2]
                ks2 = head[i][(len(head[i]) // 2)+1:]
                if (ks1 == tail[i][:len(head[i]) // 2]) and (ks2 == tail[i][(len(head[i]) // 2)+1:]):
                    s += 1
                    continue
            else: 
                ks1 = head[i][:(len(head[i]) // 2)-1]
                ks2 = head[i][(len(head[i]) // 2):]
                if (ks1 == tail[i][:(len(head[i]) // 2)-1]) and (ks2 == tail[i][(len(head[i]) // 2):]):
                    s += 1
                    continue
            if len(head[i]) % 2 != 0:
                ks1 = head[i][:len(head[i]) // 2]
                ks2 = head[i][(len(head[i]) // 2)+1:]
                if (ks1 == tail[i][:len(head[i]) // 2]) and (ks2 == tail[i][(len(head[i]) // 2)+1:]):
                    s += 1
                    continue

    if (f == len(head)) and (s == len(head)):
        print("Тип 1: неукорачивающая и контекстно-зависимая")
    elif (f == len(head)) and (s != len(head)):
        print("Тип 1: неукорачивающая")
        if (f != len(head)) and (s == len(head)):
            print("Тип 1: контекстно-зависимая")
              

N = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
kol_symbols = int(input("Кол-во букв в алфавите: "))
T = []
for i in range(kol_symbols):
    Simb = input('Введите букву алфавита: ')
    while Simb in T:
        Simb = input('Введите другую букву алфавита: ')
    T.append(Simb)

kol_leks = int(input("Кол-во лексем: "))
leksems_head = []
leksems_tail = []
for i in range(kol_leks):
    l = input("Лексема(Ввод через пробел): ")
    l = l.split(" ")
    if l[1].find("/") != -1:
        l2 = l[1].split("/")
        for i in l2:
            leksems_head.append(l[0])
            leksems_tail.append(i)
    else:
        leksems_head.append(l[0])
        leksems_tail.append(l[1])

print("-----------------------------")
thirdtype(N, leksems_head, leksems_tail)
if secondtype(leksems_head) == True:
    print("Тип 2: контекстно-свободная")
firsttype(leksems_head, leksems_tail)
print("Обязательно тип 0!")





8