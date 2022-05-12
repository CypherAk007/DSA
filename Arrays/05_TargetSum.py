arr = [10,5,2,2,1,3,6,-6,11]
val =[]
s = 4
# print("cypherAk")
for i in range(len(arr)):
    # print(arr[i])
    for j in range(i+1,len(arr)):
        if(arr[i]!=arr[j]):
            if((arr[i]+arr[j])==s):
                if((arr[i],arr[j]) not in val):
                    val.append((arr[i],arr[j]))
                # print(arr[i],arr[j])
              
print(val)


