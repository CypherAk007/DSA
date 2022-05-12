from multiprocessing.sharedctypes import Value


lst = [1,2,3,4,5,6,7]
twoDl=[[1,2,3],[4,5,6]]
# 1.Traversing empty list return ntg
def traverseEmptyList(list):
  for i in list:
    print(i)

# 2.  updating - O(1) and insert - O(n)
def updateList(list,index,value):
  print(list)
  list[index]=value
  print(list)

def insertInList(list,index,value):
  print(list)
  list.insert(index,value)
  print(list)

# 3. append(value)- O(1) extend(newList)-O(n)loops the value of new list

# 4. update multiple elements in the list
def updatelst(lst):
  print(lst)
  lst[0:2]= ['x','y']
  print(lst[:])

# 5.deletion with pop() method-index
def delPop(lst,index):
  print(lst)
  print(lst.pop(index))
  print(lst)
  

# 6.deletion using delete method-index
def delDelete(lst,index):
  print(lst)
  del lst[index]
  print(lst)
  del lst[0:2]
  print(lst)

# 7.deletion using remove - Value
def delRemove(lst,value):
  print(lst)
  lst.remove(value)
  print(lst)

# 8. twoDlst operations
def twoDlstOp(twoD):
  print(len(twoD))#no.of rows
  print(len(twoD[0]))#no. of col

# 9.que
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: 
              sv = element
 
    return v


# traverseEmptyList([])
# updateList(lst,2,33)
# insertInList(lst,0,11)
# updatelst(['a','b','c','d'])
# delPop(['a','b','c','d'],2)
# delDelete(['a','b','c','d'],3)
# delRemove(['a','b','c','d'],'c')
twoDlstOp(twoDl)
print(fun(data[0]))