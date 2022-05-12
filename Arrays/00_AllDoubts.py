# 1.
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v

print(fun(data[0]))
# op->4

# 2.
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)
# op->attempt to assign sequence of size 6 to extended slice of size 5