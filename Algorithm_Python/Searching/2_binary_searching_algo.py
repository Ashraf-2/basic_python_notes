# this is a code file of Binary Searching Algorithm
import math
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

length = len(li)
# print(len)
l_o = 0
h_o = length-1
# print(l_o,h_o)
lookUp_value = int(input("Your Lookup Value: "))
# lookUp_value = 8

# print(math.floor(8.9))
def binary_search(numbers,x,lowestOrder, highestOrder):
       while True:
        avg_index = math.floor((lowestOrder+highestOrder)/2)
        # print(math.floor(avg_index))
        # print(li[math.floor(avg_index)])
        # print(avg_index)
        # break
        if (x == numbers[avg_index]):
            return avg_index
        elif(x > numbers[avg_index]):
            lowestOrder = avg_index
            highestOrder = numbers[length-1]
            # highestOrder = len(numbers)-1
            highestOrder = length-1
        elif(x < numbers[avg_index]):
            lowestOrder = lowestOrder
            highestOrder = avg_index
        else:
            print("Your lookup value does not exist in this number of list")
            return False

pointer = binary_search(li,lookUp_value,l_o,h_o)
print("Your lookup value '",lookUp_value,"' is in the index number:",pointer)

