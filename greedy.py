def quicksort(listToSort):
    less = []
    more = []
    equal = []
    if len (listToSort) > 1:
        pivot = listToSort[0]
        for i in listToSort:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                more.append(i)
        return quicksort(more)+equal+quicksort(less)
    else:
        return listToSort 
        
def greSubsetSum(listToSort,tot):
    sortedList = quicksort(listToSort)
    print("Sorted List: ",sortedList)
    current = 0
    used = []
    for i in range(len(sortedList)):
        if current < tot:
            current = current + sortedList[i]
            if current > tot:
                current = current - sortedList[i]
            else:
                used.append(sortedList[i])
        elif current == tot:
            return used
        else:
            return None

listToSend = [1,2,3,4,5,6,7,8]
totalToSend = 12
print("Set: ", listToSend) #prints out set
print("Total: ", totalToSend) #prints total
out = greSubsetSum(listToSend, totalToSend) #calls the dynSubsetSum method and hads the set and the total
print("Results: ", out) #prints out the values that sum to the total      
