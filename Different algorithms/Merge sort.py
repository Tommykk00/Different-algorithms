def merge(listA, listB):
    newList = list()
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1

    while a < len(listA):
        newList.append(listA[a])
        a += 1
    while b < len(listB):
        newList.append(listB[b])
        b += 1
    return newList

def mergeSort(inputList):
    if len(inputList) <= 1:
        return inputList
    else:
        mid = len(inputList) // 2
        left = mergeSort(inputList[:mid])
        right = mergeSort(inputList[mid:])
        newList = merge(left, right)
        return newList

a = [12, 67, 43, 877, 23, 96, 18, 92]
a = mergeSort(a)

print("Sorted array is: ")
for i in range(len(a)):
    print("%d" %a[i])
    
