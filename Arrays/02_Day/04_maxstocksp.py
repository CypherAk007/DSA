def stocksp(prices):
  maxProfit = 0
  minDayPrice = float('inf')
  for i in range(len(prices)):
    if prices[i]<minDayPrice:
      minDayPrice = prices[i]
    if maxProfit<prices[i]-minDayPrice:
      maxProfit = prices[i]-minDayPrice
  return maxProfit


prices = [7,1,5,3,6,4]
print(stocksp(prices))