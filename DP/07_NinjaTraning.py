# Ninja is planing this ‘N’ days-long training schedule. Each day, he can perform any one of these three activities. 
# (Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. 
# As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days. 
# Can you help Ninja find out the maximum merit points Ninja can earn?
# You are given a 2D array of size N*3  ‘POINTS’ with the points corresponding to each day and activity.
# Your task is to calculate the maximum number of merit points that Ninja can earn.
# [[1,2,5], [3 ,1 ,1] ,[3,3,3] ]

class Ninja:
  def ninjaTraining(self,n,days):
    last=3# this tells about the task selected previously 3->non selected
    dp=[[-1]*4 for i in range(n)]
    return self.ninja(n-1,last,days,dp)

  def ninja(self,day,last,points,dp):
    if day==0:
      maxi=0
      for task in range(3):
        if task!=last:
          maxi=max(maxi,points[0][task])
      return maxi

    if dp[day][last]!=-1:
      return dp[day][last]

    maxi=0
    for task in range(0,3):
      if task!=last:
        point=points[day][task]+self.ninja(day-1,task,points,dp)
        maxi=max(maxi,point)
    dp[day][last]=maxi 
    return dp[day][last]

  def ninjaTrainingTab(self,n,points):
    last=3# this tells about the task selected previously 3->non selected
    dp=[[-1]*4 for i in range(n)]
    dp[0][0]=max(points[0][1],points[0][2])
    dp[0][1]=max(points[0][0],points[0][2])
    dp[0][2]=max(points[0][0],points[0][1])
    dp[0][3]=max(points[0][0],max(points[0][1],points[0][2]))
    for day in range(1,n):
      for last in range(0,4):
        dp[day][last]=0
        maxi=0
        for task in range(0,3):
          if task!=last:
            point=points[day][task]+dp[day-1][task]
            maxi=max(maxi,point)
        dp[day][last]=maxi 

    return dp[n-1][3]
ni=Ninja()
days=[[1,2,5], [3 ,1 ,1] ,[3,3,3]]
n=len(days)
print(ni.ninjaTraining(n,days))
print(ni.ninjaTrainingTab(n,days))