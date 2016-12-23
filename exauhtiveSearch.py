class SSP():
    def exaSubsetSum(self, list1, tot):

        if tot == 0 or tot < 1: #if the total is equal to 0 for less then 1 it ends
            return None
        elif len(list1) == 0: #if the list is empty it ends
            return None
        else: #when passed the checks above
            if list1[0] == tot: #if the first item in the list is the desired total it returns it
                return [list1[0]]
            else:
                search = instance.exaSubsetSum(list1[1:], (tot - list1[0])) #sets search to an instance of exaSubsetSum where the current start of the list is removed and the total has the current first item removed from it
                if search: #if search isnt empty
                    return [list1[0]] + search #returns current first item in the list plus the current value of search
                else: #if search is empty
                    return instance.exaSubsetSum(list1[1:],tot) #recursivly calls exaSubsetSum with first item removed from the list and the current total 
listToSend = [1,2,3,4,5,6,7,8]
totalToSend = 12
instance = SSP() #creates an instance of SSP dfaclass
out = instance.exaSubsetSum(listToSend, totalToSend) #calls the exaSubsetSum method and hads the set and the total
print("Set: ", listToSend) #prints out set
print("Total: ", totalToSend) #prints total
print("Results: ", out) #prints out the values that sum to the total