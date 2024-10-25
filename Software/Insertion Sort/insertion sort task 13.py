def fillArray():
    import random
    return [random.randint(10,99) for i in range(10)]

def notesInsertionSort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while arr[j-1] > temp and j > 0:    
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1

    return arr


def myInsertionSort(arr):
    for i in range(len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:    
            arr[j], arr[j-1] = arr[j-1], arr[j]

            j -= 1

    return arr



arr = fillArray()
print("arr", arr)

print(myInsertionSort(arr))
# print(notesInsertionSort(arr))