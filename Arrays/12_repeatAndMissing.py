# You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.
# Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N] which appears in the array twice and another number M in the range [1, N] which is missing from the array.
# Your task is to find the missing number (M) and the repeating number (R).

# Example:
# Input:[3 1 2 5 3] 
# Output:[3, 4] 
# A = 3, B = 4

def repeatedNumber( A):
        dupNo=0
        sumNo=0
        leftNo=0
        lst=[]
        x=1
        for i in range(len(A)):
            leftNo+=x
            sumNo+=abs(A[i])
            x+=1
            if A[abs(A[i])-1]<0:
                dupNo=abs(A[i])
            else:
                A[abs(A[i])-1]=-A[abs(A[i])-1]
        sumNo-=dupNo
        if leftNo-sumNo>dupNo:
            lst.append(dupNo)
            lst.append(leftNo-sumNo)
        else:
            lst.append(leftNo-sumNo)
            lst.append(dupNo)
        return lst   

A=[]
print(repeatedNumber([3,1,2,5,3]))