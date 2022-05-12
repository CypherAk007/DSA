from calendar import c
import math
from tkinter.tix import Tree
from unicodedata import digit

def printDesc(n):
    if n==0:
        return
    print(n)
    printDesc(n-1)

def printIncreasing(n):
    if n==0:
        return
    printIncreasing(n-1)
    print(n)
    
def retDescLst(n):
    if n==0:
        blst=[]
        return blst
    lst=[]
    lst.append(n)
    rlst=retDescLst(n-1)
    lst+=rlst
    return lst

def retIncLst(n,lst):
    if n==0:
        return
    retIncLst(n-1,lst)
    lst.append(n)
    
def printIncDesc(n):
    if n==0:
        blst=[]
        return blst
    lst=[]
    lst.append(n)
    rlst=printIncDesc(n-1)
    lst+=rlst
    lst.append(n)
    return lst
    
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
    
def powof(x,n):
    if n==0:
        return 1
    rop=powof(x,n-1)
    out=x*rop
    return out
    
def optiPowOf(x,n):
    if n==0:
        return 1
    ro=optiPowOf(x,n//2)
    totpow=ro*ro
    if n%2==1:
        totpow=totpow*x
    return totpow
    
def TOH(n,A,B,C):
    if n==0:
        return
    TOH(n-1,A,C,B)
    print(f'{n} is moved fm {A} -> {B}')
    TOH(n-1,C,B,A)


def displayArr(a,idx):
    if idx==len(a):
        return
    print(a[idx])
    displayArr(a,idx+1)   

def displayArrRev(a,idx):
    if idx==len(a):
        return 
    displayArrRev(a,idx+1)
    print(a[idx])

def maxOfArray(arr,idx):
    if idx==len(arr)-1:
        return arr[idx]
    cmax=maxOfArray(arr,idx+1)
    if arr[idx]>cmax:
        return arr[idx]
    else:
        return cmax

def firstOccArr(arr,idx,target):
    if idx==len(arr):
        return -1

    if arr[idx]==target:
        return idx
    out=firstOccArr(arr,idx+1,target)
    return out
    
def lastIdxArr(arr,idx,target):
    if idx==len(arr):
        return -1
    ra=lastIdxArr(arr,idx+1,target)
    if ra==-1:
        if arr[idx]==target:
            return idx
        else:
            return -1
    else:
        return ra

def allIndexArr(arr,idx,target,c):
    if idx==len(arr):
        blst=[0]*c
        return blst

    if arr[idx]==target:
        clst=allIndexArr(arr,idx+1,target,c+1)
        clst[c]=idx
        return clst
    else:
        clst=allIndexArr(arr,idx+1,target,c)
        return clst

def sumTri(arr):
    if len(arr)==0:
        # print(arr[0])
        return
    lst=[]
    for i in range(len(arr)-1):
        lst.append(arr[i]+arr[i+1])
    sumTri(lst)
    print(arr)

def binarySearch(l,h,target,arr):
    if l>h:
        return -1
    else:
        mid=(l+h)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            mans=binarySearch(l,mid-1,target,arr)
            return mans
        mans=binarySearch(mid+1,h,target,arr)
        return mans

def revstr(s):
    if len(s)==0:
        return ''
    ch=s[0]
    ros=s[1:]
    bret=revstr(ros)
    bret+=ch
    return bret

def fib(n):
    if n<2:
        return n
    return fib(n-1)+ fib(n-2)

def sumofdig(n):
    if n==0:
        return 0
    u=n%10
    out=sumofdig(n//10)
    out+=u
    return out

def revANo(num):
    if num==0:
        return 0

    u=num%10
    s=int(math.log(num,10))
    bout=revANo(num//10)
    bout+=u*(pow(10,s))
    return bout

def countNoOfZero(num):
    if num==0:
        return 0
    count=0
    if num%10==0:
        count=1
    out= countNoOfZero(num//10)
    out+=count
    return out

def checkSort(arr,idx):
    if idx==len(arr)-1:
        return True
    if arr[idx]>arr[idx+1]:
        return False
    bout=checkSort(arr,idx+1)
    return bout

def printrevstarpattern(r,c):
    if r==0:
        return

    if c<r:
        printrevstarpattern(r,c+1)
        print('x',end=' ')
    else:
        printrevstarpattern(r-1,0)
        print('\n')

def bs(arr,r,c):
    if r==0:
        return

    if c<r: 
        if arr[c]>arr[c+1]:
            arr[c],arr[c+1]=arr[c+1],arr[c]
        bs(arr,r,c+1)
    else:
        bs(arr,r-1,0)

def ss(arr,r,c,maxi):
    if r==0:
        return
    if c<r:
        if arr[c]>arr[maxi]:
            ss(arr,r,c+1,c)
        else:
            ss(arr,r,c+1,maxi)
    else:
        arr[r-1],arr[maxi]=arr[maxi],arr[r-1]
        ss(arr,r-1,0,0)
    

def ms(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    larr=arr[:mid]
    rarr=arr[mid:]
    left=ms(larr)
    right=ms(rarr)
    return merge(left,right)

def merge(left,right):
    i=0
    j=0
    k=0
    llen=len(left)
    rlen=len(right)
    out=[0]*(llen+rlen)
    while(i<llen and j<rlen):
        if left[i]<right[j]:
            out[k]=left[i]
            i+=1
        else:
            out[k]=right[j]
            j+=1
        k+=1
    
    while(i<llen):
        out[k]=left[i]
        k+=1
        i+=1

    while(j<rlen):
        out[k]=right[j]
        k+=1
        j+=1

    return out


def msInplace(arr,s,e):
    if e-s==1:
        return
    mid=(s+e)//2
    msInplace(arr,s,mid)
    msInplace(arr,mid,e)
    return mergeInplace(arr,s,e,mid)

def mergeInplace(arr,s,e,mid):
    i=s
    j=mid
    k=0
    out=[0]*(e-s)
    while(i<mid and j<e):
        if arr[i]<arr[j]:
            out[k]=arr[i]
            i+=1
        else:
            out[k]=arr[j]
            j+=1
        k+=1
    
    while(i<mid):
        out[k]=arr[i]
        k+=1
        i+=1

    while(j<e):
        out[k]=arr[j]
        k+=1
        j+=1

    for k in range(len(out)):
        arr[s+k]=out[k]

def qs(arr,l,h):
    if l>=h:
        return

    s=l
    e=h
    mid=s+(e-s)//2
    pivot=arr[mid]
    while(s<=e):
        while(arr[s]<pivot):
            s+=1
        while(arr[e]>pivot):
            e-=1

        if s<=e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1

    qs(arr,l,e)
    qs(arr,e,h)

def removeTarget(s,t):
    if len(s)==0:
        return ''
    ch=s[0]
    if ch==t:
        out=removeTarget(s[1:],t)
        return out
    else:
        out=removeTarget(s[1:],t)
        return ch+out

def removeadjsameele(s,t):
    if len(s)==0:
        return ''
    ch=s[0]
    if s[0]==t:
        print(f'1->{s},{t}')
        out=removeadjsameele(s[1:],t)
        return out
    else:
        t=ch
        print(f'2->{s},{t}')
        out=removeadjsameele(s[1:],t)
        return ch+out
    
def subset(p,up):
    if len(up)==0:
        print(p)
        return
    ch=up[0]
    #take
    subset(p+ch,up[1:])
    #leave
    subset(p,up[1:])

def subsetlst(p,up):
    if len(up)==0:
        lst=[]
        lst.append(p)
        return lst

    ch=up[0]
    take=subsetlst(p+ch,up[1:])
    leave=subsetlst(p,up[1:])
    take+=leave
    return take


def permutations(p,up):
    if len(up)==0:
        print(p)
        return
    ch=up[0]
    for i in range(0,len(p)+1):
        f=p[0:i]
        s=p[i:len(p)]
        permutations(f+ch+s,up[1:])

def keypad(p,up):
    if len(up)==0:
        print(p)
        return
    digit=int(up[0])
    for i in range((digit-1)*3,digit*3):
        ch = chr(97+i)
        keypad(p+ch,up[1:])

def dice(p,up):
    if up==0:
        print(p)
        return

    for i in range(1,7):
        if i<=up:
            dice(p+str(i),up-i)

def cntmaze(r,c):
    if r==1 or c==1:
        return 1
    down=cntmaze(r-1,c)
    right=cntmaze(r,c-1)
    return down + right

def printMaze(p,r,c):
    if r==1 and c==1:
        print(p)
        return
    if r>1:
        printMaze(p+'D',r-1,c)
    if c>1:
        printMaze(p+'R',r,c-1)
    
def Mazelst(p,r,c):
    if r==1 and c==1:
        lst=[]
        lst.append(p)
        return lst
    out=[]
    if r>1:
        out+=Mazelst(p+'D',r-1,c)
    if c>1:
        out+=Mazelst(p+'R',r,c-1)
    return out

def Mazelstdiag(p,r,c):
    if r==1 and c==1:
        lst=[]
        lst.append(p)
        return lst
    out=[]
    if r>1:
        out+=Mazelstdiag(p+'V',r-1,c)
    if r>1 and c>1:
        out+=Mazelstdiag(p+'D',r-1,c-1)
    if c>1:
        out+=Mazelstdiag(p+'H',r,c-1)
    return out

def mazeWtObst(p,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        lst=[]
        lst.append(p)
        return lst
    if maze[r][c]==False:
        return ''
    out=[]
    if r<len(maze)-1:
        out+=mazeWtObst(p+'D',maze,r+1,c)
    if c<len(maze[0])-1:
        out+=mazeWtObst(p+'R',maze,r,c+1)
    return out


if __name__=='__main__':
  # printDesc(5)
  
  # printIncreasing(5)
  
  # print(retDescLst(5))
  
  # lst=[]
  # retIncLst(5,lst)
  # print(lst)
  
  # print(printIncDesc(5))
  
  # print(fact(5))
  
  # x=3
  # n=3
  # print(powof(x,n))
  
  # x=3
  # n=3
  # print(optiPowOf(x,n))
  
  # A='A'
  # B='B'
  # C='C'
  # n=3
  # TOH(n,A,B,C)

    # a=[1,2,3,4,5]
    # idx=0
    # displayArr(a,idx)

    # a=[1,2,3,4,5]
    # idx=0
    # displayArrRev(a,idx)

    # arr=[1,2,30,4,5]
    # idx=0
    # print(maxOfArray(arr,idx))

    # arr=[1,2,30,4,5]
    # idx=0
    # target=4
    # print(firstOccArr(arr,idx,target))

    # arr=[1,2,5,30,4,5]
    # idx=0
    # target=5
    # print(lastIdxArr(arr,idx,target))

    # arr=[1,2,5,30,5,4,5]
    # idx=0
    # target=5
    # c=0
    # print(allIndexArr(arr,idx,target,c))

    # arr=[1,2,3,4,5]
    # sumTri(arr)

    # arr=[1,2,3,4,5]
    # l=0
    # h=len(arr)-1
    # target=6
    # print(binarySearch(l,h,target,arr))

    # s='abcde'
    # print(revstr(s))

    # print(fib(7))

    # print(sumofdig(12345))
    
    # num=1234
    # print(revANo(num))

    # num=1020304
    # print(countNoOfZero(num))

    # arr=[1,2,3,4,6,5]
    # print(checkSort(arr,0))


    # printrevstarpattern(4,0)

    # arr=[5,4,3,2,1]
    # bs(arr,len(arr)-1,0)
    # print(arr)


    # arr=[5,3,4,2,1]
    # ss(arr,len(arr),0,0)
    # print(arr)

    # arr=[8,3,4,12,5,6]
    # print(ms(arr))

    # arr=[81,3,4,12,5,6]
    # msInplace(arr,0,len(arr))
    # print(arr)

    # arr=[81,3,4,12,5,6]
    # qs(arr,0,len(arr)-1)
    # print(arr)

    # s='abbcccdcdde'
    # t=s[0]
    # print(removeadjsameele(s[1:],t))
    # print(s)

    # s='abbcccdcdde'
    # t='c'
    # print(removeTarget(s,t))

    # p=''
    # up='abc'
    # subset(p,up)

    # p=''
    # up='abc'
    # print(subsetlst(p,up))

    # p=''
    # up='abc'
    # permutations(p,up)

    # p=''
    # up='12'
    # keypad(p,up)

    # p=''
    # up=4
    # dice(p,up)

    # print(cntmaze(3,3))
    # print(Mazelst('',3,3))
    # print(Mazelstdiag('',3,3))

    maze=[[True,True,True],
            [True,False,True],
            [True,True,True]]
    print(mazeWtObst('',maze,0,0))