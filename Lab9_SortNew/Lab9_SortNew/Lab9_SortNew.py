import random
from isSorted import isSorted

comp = 0

def quickSortList1(ll):
    global comp
    if len(ll) > 1:
        pivot = 0
        #pivot = len(ll) // 2
        # pivot = len(ll) - 1

        leftList = []
        rightList = []

        for i in range(0,len(ll)):
            comp += 1
            if i == pivot:
                continue
            if ll[i] <= ll[pivot]:
                leftList.append(ll[i])
            else:
                rightList.append(ll[i])

        leftList = quickSortList1(leftList)
        rightList = quickSortList1(rightList)
        leftList.append(ll[pivot])
        return leftList + rightList
    return ll

def quickSortList2(ll):
    global comp
    if len(ll) > 1:
        # pivot = 0
        #pivot = len(ll) // 2
        pivot = len(ll) - 1

        leftList = []
        rightList = []

        for i in range(0,len(ll)):
            comp += 1
            if i == pivot:
                continue
            if ll[i] <= ll[pivot]:
                leftList.append(ll[i])
            else:
                rightList.append(ll[i])

        leftList = quickSortList2(leftList)
        rightList = quickSortList2(rightList)
        leftList.append(ll[pivot])
        return leftList + rightList
    return ll

def quickSortList3(ll):
    global comp
    if len(ll) > 1:
        # pivot = 0
        pivot = len(ll) // 2
        # pivot = len(ll) - 1

        leftList = []
        rightList = []

        for i in range(0,len(ll)):
            comp += 1
            if i == pivot:
                continue
            if ll[i] <= ll[pivot]:
                leftList.append(ll[i])
            else:
                rightList.append(ll[i])

        leftList = quickSortList3(leftList)
        rightList = quickSortList3(rightList)
        leftList.append(ll[pivot])
        return leftList + rightList
    return ll
list = []
l1 = []
l2 = []
l3 = []

#0
#list.append(5)

#1
#for i in range (0,21):
#    list.append(i)

#2
#for i in range (20,0,-1):
#    list.append(i)

#3 random
for i in range(0,20):
    rand = random.randint(1,100)
    list.append(rand)

print(list)

comp = 0
l1 = quickSortList1(list)
print("#1 - ", comp, " ==> ", end = "")
print(l1)

comp = 0
l2 = quickSortList2(list)
print("#2 - ", comp, " ==> ", end = "")
print(l2)

comp = 0
l3 = quickSortList3(list)
print("#3 - ", comp, " ==> ", end = "")
print(l3)

