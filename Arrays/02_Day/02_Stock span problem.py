# The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stocks price for all n days. 
# The span Si of the stocks price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
# For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

# Example 1:

# Input: 
# N = 7, price[] = [100 80 60 70 60 75 85]
# Output:
# 1 1 1 2 1 4 6
# Explanation:
# Traversing the given input span for 100 
# will be 1, 80 is smaller than 100 so the 
# span is 1, 60 is smaller than 80 so the 
# span is 1, 70 is greater than 60 so the 
# span is 2 and so on. Hence the output will 
# be 1 1 1 2 1 4 6.

def calculateSpan(self,a,n):
        out=[]
        s=[]

        for i in range(0,len(a)):
             # inital
            if len(s)==0:
                out.append(1)
            if len(s)>0 and a[i]<s[-1][0]:
                out.append(abs(i-s[-1][1]))
                
            elif len(s)>0 and a[i]>=s[-1][0]:
                while(len(s)>0 and a[i]>=s[-1][0]):
                    s.pop()
                # if stack is empty
                if len(s)==0:
                    out.append(i+1)
                else:
                    out.append(abs(i-s[-1][1]))
            s.append((a[i],i))  
        return(out) 