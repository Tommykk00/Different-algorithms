#This algorithm sorts numbers to rising order

import sys

a = [157, 89, 775, 12, 37]
 
# Traverse through all array elements
for i in range(len(a)):
     
    # Find the minimum element in remaining unsorted array
    minidx = i
    for j in range(i+1, len(a)):
        if a[minidx] > a[j]:
            minidx = j
             
    # Swap the found minimum element with the first element       
    a[i], a[minidx] = a[minidx], a[i]
 
# Driver code
print ("Sorted array is: ")
for i in range(len(a)):
    print("%d" %a[i]),
