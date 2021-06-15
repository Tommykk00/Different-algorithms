#This algorithm sorts numbers in rising order

def bubbleSort(arr):
    n = len(arr)

    #go through all array elements
    for i in range(n):

        #last i elements are already in place
        for j in range(0, n - i - 1):

            #traverse the array from 0 to n-i-1
            #swap if element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#driver code
arr = [55, 44, 74, 26, 12, 90, 81, 123, 654, 2, 16]
bubbleSort(arr)

print("Sorted array is: ")
for i in range(len(arr)):
    print("%d" %arr[i])
            
