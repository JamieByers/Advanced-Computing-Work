def readFile():
    arr = [[] for _ in range(3)]

    with open("movies.csv", "r") as file:
        for line in file.readlines():
            line = line.strip("\n")
            line = line.split(",")

            arr[0].append(line[0])
            arr[1].append(int(line[1]))
            arr[2].append(int(line[2]))

    return arr 

arr = readFile()

def bubbleSortDescBox(arr):
    swapped = True
    length = len(arr[1])

    while length >= 0 and swapped:
        swapped = False
        for i in range(length-1):
            if arr[1][i] < arr[1][i+1]:
                arr[1][i], arr[1][i+1] = arr[1][i+1], arr[1][i]
                arr[0][i], arr[0][i+1] = arr[0][i+1], arr[0][i]
                arr[2][i], arr[2][i+1] = arr[2][i+1], arr[2][i]
                
                swapped = True
        length -= 1

    return arr

arr = bubbleSortDescBox(arr)
print(arr)
