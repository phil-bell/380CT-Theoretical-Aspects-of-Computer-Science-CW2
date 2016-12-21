class SSP():
    def subsetSum(self, list1, tot):
        table = [[0 for a in range(tot)] for b in range(len(list1))]
        print (table)
        for i in range(1, tot):
            table[0][i] = 0
        print (table)
        for i in range(0, len(list1)):
            table[i][0] = 1
        print (table)
        for i in range(1, len(list1)):
            print ("Attempt: ",i)
            print (table)
            for j in range(1,tot):
                table[i][j] = table[i-1][j]
                print (table)
                if table[i][j]==0 and j>=list1[i-1]:
                    table[i][j] = table[i][j] or table[i-1][j-list1[i-1]]
                    print (table)
        return table[len(list1)-1][tot-1]

listToSend = [1,2,3]
totalToSend = 5
instance = SSP()
out = instance.subsetSum(listToSend,totalToSend)
print ("Set: ",listToSend) #prints out set
print ("Total: ",totalToSend) #prints total
print ("Results: ",out) #prints out the values that sum to the total