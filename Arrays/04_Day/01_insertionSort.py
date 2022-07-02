def insertionSort(a):
    for i in range(len(a)):
        temp=a[i]
        j=i-1
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp

a=[12, 11, 13, 5, 6]
insertionSort(a)
print(a)