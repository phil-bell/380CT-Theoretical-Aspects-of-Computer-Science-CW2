class SSP():
    def subsetSum(self, list1, tot):
        table = [len(list1)+1][tot+1]
        for i in range(0, tot):
            table[0][i] = False

        for i in range(0, len(list1)):
            table[i][0] = True

        for i in range(0, len(list1)):
            for j in range(0,tot):
                table[i][j] = table[i-1][j]
                if table[i][j]==False and j>=list1[i-1]:
                    table[i][j] = table[i][j] or table[i-1][j-list1[i-1]]
        return table[len(list1)][tot]

listToSend = [1,2,3,4,5,6,7,8]
totalToSend = 12
instance = SSP()
out = instance.subsetSum(listToSend,totalToSend)
print ("Set: ", listToSend) #prints out set
print ("Total: ", totalToSend) #prints total
print ("Results: ",out) #prints out the values that sum to the total