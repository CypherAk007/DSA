matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(len(matrix))# row value
print(len(matrix[0]))# column value
transposed = []
for i in range(4):
  lst=[]
  for j in matrix:
    # print(j)
    lst.append(j[i])
    # print(lst)
  transposed.append(lst)

for i in transposed:
  print(i)