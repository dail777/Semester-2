myList = [5, 2, 9, 1, 5, 6]
swapped = True

print("Unsorted list:", myList)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
            swapped = True

print("Sorted list:", myList)