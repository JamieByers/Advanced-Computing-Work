class State:
    capital = ""
    name = ""
    abv = ""

def readFile():
    arr = []
    with open("states.txt", "r") as file:
        for line in file.readlines():
            line = line.strip("\n").split(",")

            s = State()

            s.capital = line[0]
            s.name = line[1]
            s.abv = line[2]

            arr.append(s)

    return arr

arr = readFile()

def insertionSort(arr):
    for i in range(len(arr)):
        value1 = arr[i].capital
        value2 = arr[i].name
        value3 = arr[i].abv
        j = i
        while j>0 and value2 < arr[j-1].name:
            arr[j].capital = arr[j-1].capital
            arr[j].name = arr[j-1].name
            arr[j].abv = arr[j-1].abv
            j -= 1
        arr[j].capital = value1
        arr[j].name = value2
        arr[j].abv = value3

    return arr 

arr = insertionSort(arr)

for i in arr:
    print(i.name)