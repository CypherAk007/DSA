from array import *
import numpy as np

arr1 = array('i',[1,2,3,4,5,6])
twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]]) #creating 2d array

# 1. Create array and traverse.
def arrTraverse(arr):
  for i in arr:
    print(i)

# 2. Access individual elements through indexes
def accessEle(arr,index):
  if index<len(arr):
    print(arr[index])
  else:
    print("index out of range")

# 3. Append any value to the array using append() method(appends at the end of the array)-O(1)
def appendEle(arr,value):
  print(arr)
  arr.append(value)
  print(arr)

# 4. Insert value into the array 
def insertEle(arr,index,value):
  arr.insert(index,value)
  print(arr)


# 5.Extend the array using extend() method
def extendArr(arr,extraArr):
  arr.extend(extraArr)
  print(arr)

# 6.Add items from list into array using fromlist() method
def listInArr(arr,list):
  arr.fromlist(list)
  print(arr)

# 7.Remove the last element
def removelast(arr):
  arr.pop()
  print(arr)

# 8.find the index of element given the element
def index(arr,value):
  print(arr.index(value))

# 9.get array buffer information
def bufferInfo(arr):
  print(arr.buffer_info()) #prints the array start buffer and the no. of elements in it.

# 10.check for no. of occurances of an element using count() method
arr1.append(1)
def countOcc(arr,value):
  print(arr.count(value))


# 11.convert array to list
def arrToList(arr):
  print(arr)
  print(arr.tolist())

# 12.sliceing
def slicing(arr):
  print(arr[1:4]) #prints the first 3 elements
  print(arr[2:]) #prints from the 2nd element
  print(arr[:]) #prints all the elements

# 2D Array
#13.print 2d array
def printOriginal2DArray(twoD):
  print(twoD) 

# 14. insert column in 2d array O(n^2)
def insertColumn(twoD,position,column,axis): #position- which row/column no., axis- 0=row 1=column
  print(twoD)
  print('\n')
  newTwoD = np.insert(twoD,position,column,axis)
  print(newTwoD)

# 15. insert row in 2d array O(n^2)
def insertRow(twoD,position,row,axis): #position- which row/column no., axis- 0=row 1=column
  print(twoD)
  print('\n')
  newTwoD = np.insert(twoD,position,row,axis)
  print(newTwoD)

# 16. insert row in 2d array at end O(1)
def appendRow(twoD,row,axis): #position- which row/column no., axis- 0=row 1=column
  print(twoD)
  print('\n')
  newTwoD = np.append(twoD,row,axis)
  print(newTwoD)

# 17. accessElement in 2d array O(1)
def access2dElement(array, rowIndex, colIndex):
  print(array)
  if rowIndex >= len(array) or colIndex>= len(array[0]): # len(array)->no.of rows len(array[0])- no.of columns
    print("invalid indexes")
  else:
    print(array[rowIndex][colIndex])
  
# 20. traverse 2d array O(n^2)
def traverse2dArray(array):
  print(array)
  for i in range(len(array)):
    for j in range(len(array[0])):
      print(array[i][j])

# 21. search element in 2d array O(n^2)
def search2dArray(array,value):
  print(array)
  for i in range(len(array)):
    for j in range(len(array[0])):
      if array[i][j]== value:
        return ([i,j])
  return 'element not found'

# 22. delete row/column from 2d array at begining - O(n^2) ;at end - O(1)
def delete2dArray(array,pos,axis):
  newTdArray = np.delete(array,pos,axis)
  print(newTdArray)



# arrTraverse(arr1)
# accessEle(arr1,6)
# appendEle(arr1,10)
# insertEle(arr1,1,222)
# extendArr(arr1,[12,13,14])
# listInArr(arr1,[23,24,25])
# removelast(arr1)
# index(arr1,222)
# bufferInfo(arr1)
# countOcc(arr1,1)
# arrToList(arr1)
# slicing(arr1)


# printOriginal2DArray(twoDArray)
# insertColumn(twoDArray,0,[[9,8,7]],1)
# insertRow(twoDArray,0,[[1,1,1]],0)
# appendRow(twoDArray,[[14,13,12]],0)
# access2dElement(twoDArray,2,2)
# traverse2dArray(twoDArray)
# print(search2dArray(twoDArray,10))
# delete2dArray(twoDArray,1,0)