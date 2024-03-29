class Solution:
  def longestCommonSubsequence(self, text1, text2):
    n=len(text1)
    m=len(text2)
    
    # dp=[[-1]*(m) for i in range(n)]
    dp=[[0]*(m+1) for i in range(n+1)]
    
    # return self.helper(n-1,m-1,text1,text2,dp) replace n-1 and m-1 with n,m(shifting indexes)
    return self.helper(text1,text2,dp)
  
  # i===i-1 and j===j-1
  # Tabulation
  def helper(self,text1,text2,dp):
    # bc
    n=len(text1)
    m=len(text2)
    for j in range(0,m+1):
      dp[0][j]=0
    for i in range(0,n+1):
      dp[i][0]=0
        
    for idx1 in range(1,n+1):
      for idx2 in range(1,m+1):
        if text1[idx1-1]==text2[idx2-1]:
          dp[idx1][idx2]=1 + dp[idx1-1][idx2-1]
        else:
          dp[idx1][idx2]=0+ max(dp[idx1-1][idx2],dp[idx1][idx2-1])
  
    
    # NOW MAKE THE ARR TO STORE THE MATCHED VARIBLES
    length=dp[n][m] # stores lcs length
    ans=[]
    out=''
    for i in range(0,length):
      ans.append('$')
    
    # NOW BACKTRACK TC-O(N+M)
    index=length-1
    i=n 
    j=m
    while(i >0 and j>0): # still s1 or s2 is not exausted
      #we check for the letters equal or not
      if text1[i-1]==text2[j-1]: # if there is match in the letters
        # store the letters 
        ans[index]=text1[i-1]
        index-=1
        # we go diagonal up
        i-=1
        j-=1
      # else max of previous row /col max[dp[i-1][j],dp[i][j-1]]
      elif(dp[i-1][j]>dp[i][j-1]):
        i-=1
      else:
        j-=1

    return out.join(ans)




if __name__=='__main__':
  s=Solution()
  text1='abcde'
  text2='bdgek'
  print(s.longestCommonSubsequence(text1, text2))