# import array as arr
from array import *
# # print("cypher Ak")
# v = list()
# for i in range(10):
#     v.append(i)
# print(v)

vals = array('i',[1,2,3,4,5])
print(*vals,sep=' ')
print(vals[2])

# newArr = array(vals.typecode,(a*a for a in vals)) #(type,value)
# # for i in newArr:
# #     print(i)
# # for i in range(len(v)):
# #     print(vals(i))



# ------------------------------------------------------------------
# Udemy- complete_dsa_py
# ------------------------------------------------------------------

#create an array
from array import *

arr1 = array('i',[1,2,3,4,5,6])
arr2 = array('d',[1.2,1.3,1.4])

# print(arr1)
# arr1.insert(0,0)
# print(arr1)
# arr1.insert(7,10)
# print(arr1)
# arr1.insert(2,22)
# print(arr1)
# arr1.insert(10,20)
# print(arr1)
# arr1.insert(20,200)
# print(arr1)
# print(arr1[9])

# Traversal
def arrTraversal(arr):
    for i in arr:
        print(i)

# Accessing
def accessEle(arr,index):
    if index >= len(arr):
        print('index out of range')
    else:
        print(arr[index])

# Searching
def searchEle(arr,value):
    for i in arr: # O(n)
        if i==value:
            return arr.index(value) # O(n)
    return "The element does not exist"
# Deletion
def deleteEle(arr,value):
    print(len(arr))
    print(arr)
    arr.remove(value)
    print(arr)
    print(len(arr))

# arrTraversal(arr1)
# accessEle(arr1,6)
# print(searchEle(arr1,1))
deleteEle(arr1,5)