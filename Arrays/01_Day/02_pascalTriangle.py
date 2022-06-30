'''
# today sol
def pascalTri(n):
    if n==1:
        print([[1]])
        return [[1]]
    
    outlst=[[1]]
    for i in range(1,n):
        temp = []
        temp.append(1)
        for ele in range(1,len(outlst[i-1])):
            temp.append(outlst[i-1][ele]+outlst[i-1][ele-1])
        temp.append(1)
        outlst.append(temp)
        # print(outlst)
    print(outlst)


pascalTri(3)

'''
'''
# past sol
def passc(numRows):
    if numRows==1:
        return [[1]]
        # if numRows==2:
        #     return [[1],[1,1]]
    outLst=[]
    # append result with lst of 1's wrt the numRows value
    for i in range(numRows):
        outLst.append([1]*(i+1))
    print(outLst)
    
    # leaving the 1st two output ie [[1],[1,1]] we calc for the remaing 
    for i in range(1,numRows):
        for j in range(1,i):
            outLst[i][j]=outLst[i-1][j-1]+outLst[i-1][j]
            # print(i,j,outLst[i][j],outLst[i-1][j-1],outLst[i-1][j])
    print(outLst)
    return outLst 

n=4
passc(n)
'''