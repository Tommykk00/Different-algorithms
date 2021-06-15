#This algorithm sorts numbers to rising order

def insertionSort(arr):

    #go through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]
        
        """
        move elements of arr[0..i-1], that are greater than key, to one position
        ahead of their current position
        """
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#driver code
arr = [145, 1, 34, 78, 33, 49, 91]
insertionSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
    print("%d" %arr[i])
