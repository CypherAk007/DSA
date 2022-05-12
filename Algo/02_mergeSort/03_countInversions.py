# Python program for implementation of MergeSort
 
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
 
# inv_count=0

def merge(arr, l, m, r):
    inv_count=0
    n1 = m - l + 1
    n2 = r - m
    
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            inv_count+=(m-i)
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    return inv_count
# l is for left index and r is right index of the
# sub-array of arr to be sorted

 
def mergeSort(arr, l, r):
    inv_count=0
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        inv_count+= mergeSort(arr, l, m)
        inv_count+= mergeSort(arr, m+1, r)
        inv_count+= merge(arr, l, m, r)
    return inv_count
 
# Driver code to test above

arr = [5,3,2,4,1]
n = len(arr)
print("Given array is")
for i in range(n):
  print("%d" % arr[i],end=" ")
 
out=mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
  print("%d" % arr[i],end=" ")
print("\n\ninversion is")
print(out)

