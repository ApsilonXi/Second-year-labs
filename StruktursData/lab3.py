from random import randint
import time
start = time.time()

def menu(a, n):
    #print(a)
    v = int(input("Сортировки:\n1. Прямое включение\n2. Прямой выбор\n3. Метод пузырька\n4. Метод Хоара\n5. Частичная сортировка\n"))
    if v == 1:
        PryamVkl(a, n)
    elif v == 2:
        Pryamah(a, n)
    elif v == 3:
        Bubble(a, n)
    elif v == 4:
        print(quiaksort(a, 0, n-1))
        print("\nВремя работы: ", (time.time() - start), '\nЧисло итераций: '+str(c), '\nЧисло сравнений: '+str(ss), '\nЧисло обменов: '+str(Ob))
    elif v == 5:
        Sorted(n)


def PryamVkl(a, n):
    s = 0
    ob = 0
    for i in range(1, n):
        x = a[i]
        j = i - 1
        while (x < a[j]) and (j >= 0):
            s += 1
            a[j+1] = a[j]
            ob += 1
            j -= 1
        a[j+1] = x
    print("\nВремя работы: ", (time.time() - start), '\nЧисло итераций: '+str(i), '\nЧисло сравнений: '+str(s), '\nЧисло обменов: '+str(ob))


def Pryamah(a, n):
    s = 0
    ob = 0
    for i in range(0, n-1):
        x = a[i]
        k = i
        for j in range(i+1, n):
            if a[j] < x:
                s += 1
                k = j
                x = a[j]
        a[k] = a[i]
        ob += 1
        a[i] = x
    print("\nВремя работы: ", (time.time() - start), '\nЧисло итераций: '+str(i), '\nЧисло сравнений: '+str(s), '\nЧисло обменов: '+str(ob))
    

def Bubble(a, n):
    s = 0
    ob = 0
    for i in range(n):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                s += 1
                x = a[j-1]
                a[j-1] = a[j]
                ob += 1
                a[j] = x
    print("\nВремя работы: ", (time.time() - start), '\nЧисло итераций: '+str(i), '\nЧисло сравнений: '+str(s), '\nЧисло обменов: '+str(ob))
    

def quiaksort(nums, fst, lst):
    global ss, Ob, c
    if fst >= lst: return
 
    i, j = fst, lst
    pivot = nums[randint(fst, lst)]
 
    while i <= j:
        while nums[i] < pivot: 
            i += 1
            ss += 1
        while nums[j] > pivot: 
            j -= 1
            ss += 1
        if i <= j:
           nums[i], nums[j] = nums[j], nums[i]
           Ob += 2
           i, j = i + 1, j - 1
    c += 1
    quiaksort(nums, fst, j)
    quiaksort(nums, i, lst)
    

def Sorted(n):
    b = [randint(20, 50) for i in range(n)]
    print(b)
    print("1. Прямая\n2. Обратная\n3. 25\n4. 50\n5. 75")
    B = []
    v = int(input())
    if v == 1:
        b.sort()
        print(b)
        print('Время работы: ', (time.time() - start))
        
    elif v == 2:
        b.sort(reverse=True)
        print(b)
        print('Время работы: ', (time.time() - start))
        
    elif v == 3:
        V = n * 0.25
        for i in range(round(V)):
            B.append(b[i])
        B.sort()
        for i in range(round(V)):
            b[i] = B[i]
        print(b)
        print('Время работы: ', (time.time() - start))
        
    elif v == 4:
        V = n * 0.5
        for i in range(round(V)):
            B.append(b[i])
        B.sort()
        for i in range(round(V)):
            b[i] = B[i]
        print(b)
        print('Время работы: ', (time.time() - start))
        
    elif v == 5:
        V = n * 0.75
        for i in range(round(V)):
            B.append(b[i])
        B.sort()
        for i in range(round(V)):
            b[i] = B[i]
        print(b)
        print('Время работы: ', (time.time() - start))
    

n = int(input("Введите количество элементов в массиве: "))
if n <= 20:
    a = [32, 45, 6, 87, 1, 2, 43, 2, 56, 43, 78, 90, 16, 73, 23, 98, 56, 76, 43, 20]
else:
    a = [randint(1, 50) for i in range(n)]


ss = 0
Ob = 0
c = 0
menu(a, n)






