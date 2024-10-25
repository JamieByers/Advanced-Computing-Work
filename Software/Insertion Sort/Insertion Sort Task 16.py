def readFile():
    arr = []

    with open("superBowl.txt", "r") as file:
        for line in file.readlines():
            line = line.strip("\n").split(",")
            temp = []

            temp.append(line[0])
            temp.append(line[1])
            temp.append(line[2])
            temp.append(line[3])

            arr.append(temp)

    return arr


arr = readFile()

def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp[1] > arr[j-1][1]:
            arr[j] = arr[j-1]
            j -= 1 
        arr[j] = temp

    return arr

arr = insertionSort(arr)

for a in arr:
    print(a)