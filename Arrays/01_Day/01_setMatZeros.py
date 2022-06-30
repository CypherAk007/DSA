'''
# ineff. code
def setZeros(a):
    zcrossz=False
    ithRow=[]
    jthCol=[]
    ithbool=False
    jthbool=False
    # Check the 0th row and 0thcol for making 0 at end
    if a[0][0]==0:
        zcrossz = True
        print('zcrossz')
    # Check if any 0 is at a[i][0] for making 0 at end
    for i in range(len(a)):
        if a[i][0]==0:
            ithRow.append(i)
            ithbool=True
            print(ithRow)
    # Check if any 0 is at a[0][j] for making 0 at end
    for j in range(len(a[0])):
        if a[0][j]==0:
            jthCol.append(j)
            jthbool=True
            print(jthCol)
    #filling 0s at i[0]and [0]j if any 0s in the matrix
    for i in range(1,len(a)):
        for j in range(1,len(a[0])):
            if a[i][j]==0:
                a[i][0]=0
                a[0][j]=0
    print(a)
    
    #make other elements of the same row 0
    for i in range(1,len(a)):
        if a[i][0]==0:
            print(i)
            for j in range(1,len(a[0])):
                if a[i][j]!=0:
                    print(i,j)
                    a[i][j]=0
    print(a)
    
    #make other elements of the same col 0
    for j in range(1,len(a[0])):
        if a[0][j]==0:
            print(j)
            for i in range(1,len(a)):
                if a[i][j]!=0:
                    print(i,j)
                    a[i][j]=0
    print(a)
    
    # check the ith row append in start for 0s and make respective row 0
    for i in ithRow:
        for j in range(1,len(a[0])):
            if a[i][j]!=0:
                print('ithRow')
                a[i][j]=0
            
     # check the jth col append in start for 0s and make respective col 0
    for j in jthCol:
        for i in range(1,len(a)):
            if a[i][j]!=0:
                print('jthCol')
                a[i][j]=0
            
    # if any ele in [i][0] make whole 0th row 0
    if ithbool:
        for i in range(len(a)):
            a[i][0]=0
    # if any ele in [0][j] make whole 0th row 0
    if jthbool:
        for j in range(len(a[0])):
            a[0][j]=0
    # [0][0] is 0
    if zcrossz:
        for i in range(len(a)):
            a[i][0]=0
            
        for j in range(len(a[0])):
            a[0][j]=0
    print(a)
a=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeros(a)

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

'''
'''
# eff same code o(1)space and o(n*m) time
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col=False
        
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                is_col=True
                
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        print(matrix)
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        print(matrix)
        
        if matrix[0][0] == 0 :
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        
        if is_col:
            for i in range(len(matrix)):
                matrix[i][0]=0

'''