class SSP():
    def subsetSum(self,list,tot):

        if tot == 0 or tot < 1: #if the total is equal to 0 for less then 1 it ends
            return None
        elif len(list) == 0: #if the list is empty it ends
            return None
        else: #when passed the checks above
            if list[0] == tot: #if the first item in the list is the desired total it returns it
                return [list[0]]
            else:
                search = instance.subsetSum(list[1:], (tot - list[0])) #sets search to an instance of subsetSum where the current start of the list is removed and the total has the current first item removed from it
                if search: #if search isnt empty
                    return [list[0]] + search #returns current first item in the list plus the current value of search
                else: #if search is empty
                    return instance.subsetSum(list[1:],tot) #recursivly calls subsetSum with first item removed from the list and the current total 
listToSend = [1,2,3,4,5,6,7,8]
totalToSend = 12
instance = SSP() #creates an instance of SSP class
out = instance.subsetSum(listToSend, totalToSend) #calls the subsetSum method and hads the set and the total
print ("Set: ",listToSend) #prints out set
print ("Total: ",totalToSend) #prints total
print ("Results: ",out) #prints out the values that sum to the total