#ask user inp and cal the avg temp
from array import *

from numpy import average

def usingInbuiltFnc():
  inp = int(input('How many days temperature?'))
  arr = array('i')
  for i in range(inp):
    userInp=input('Day '+str(i+1)+"'s high temp: ")
    arr.append(int(userInp))

  avg = average(arr)
  print(avg)

def WithoutInbuilt():
  inp = int(input('How many days temperature?'))
  arr = array('i')
  total = 0
 
  for i in range(inp):
    userInp=int(input('Day '+str(i+1)+"'s high temp: "))
    total+=userInp
   
    arr.append(int(userInp))
  avg = total/inp 
  print('Average: '+str(avg))
 
  for i in range(len(arr)):
    if arr[i] > avg:
      print('Day '+str(i+1)+ "'s temp is above avg")



# usingInbuiltFnc()
WithoutInbuilt()