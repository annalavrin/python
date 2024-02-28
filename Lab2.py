
import random
import datetime
import prettytable
import matplotlib.pyplot as plt

def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a

def QuickSort(A, fst, lst):
    if fst >= lst:
        return

    pivot = A[fst]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)

def insertion_sort(A):
    for i in range(1, len(A)):
        t = A[i]
        j = i
        while j > 0 and A[j-1] > t:
            A[j] = A[j-1]
            j -= 1
        A[j] = t

def shell_sort(A):
    sublistcount = len(A) // 2
    while sublistcount > 0:
        for startpos in range(sublistcount):
            gap_insertion_sort(A, startpos, sublistcount)
        sublistcount = sublistcount // 2

def gap_insertion_sort(A, start, gap):
    for i in range(start+gap, len(A), gap):
        currentvalue = A[i]
        position = i

        while position >= gap and A[position-gap] > currentvalue:
            A[position] = A[position-gap]
            position = position - gap

        A[position] = currentvalue

array = [5, 2, 10, 1, 7]
insertion_sort(array)
print(array)

table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время вставкой", "Время Шелла"])
x = []
y1 = []
y2 = []
y3 = []
y4 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    B = A.copy()

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка " + str(N) + " заняла " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая " + str(N) + " заняла " + str((t4 - t3).total_seconds()) + "c")

    C = A.copy()

    t5 = datetime.datetime.now()
    insertion_sort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Сортировка вставкой " + str(N) + " заняла " + str((t6 - t5).total_seconds()) + "c")

    D = A.copy()

    t7 = datetime.datetime.now()
    shell_sort(D)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Сортировка Шелла " + str(N) + " заняла " + str((t8 - t7).total_seconds()) + "c")

    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds()), str((t8 - t7).total_seconds())])

print(table)

plt.plot(x, y1, "C0", label="Пузырьковая сортировка")
plt.plot(x, y2, "C1", label="Быстрая сортировка")
plt.plot(x, y3, "C2", label="Сортировка вставкой")
plt.plot(x, y4, "C3", label="Сортировка Шелла")
plt.legend()
plt.show()
