def populate_array():
    import random 
    return [random.randint(100, 999) for i in range(100)]

arr = populate_array()
print(arr)

def bubbleSort(arr):
    length = len(arr)
    swapped = True
    while swapped and length >= 0:
        swapped = False
        for i in range(length-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        length -= 1
    return arr

print(bubbleSort(arr))

print(True if sorted(arr) else False)