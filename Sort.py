from heapq import nsmallest
myList = [1,3,5,6,9]
myNumber = 4
Final = nsmallest(2, myList, key=lambda x: abs(x-myNumber))
print(Final)
