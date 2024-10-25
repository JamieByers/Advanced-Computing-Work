class CountryRecord: 
    country = ""
    capital = ""

def readFile():
    arr = []
    with open("asia.csv", "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.split(",")
            cr = CountryRecord()

            cr.country = line[0]
            cr.capital = line[1]

            arr.append(cr)

    return arr

def binSearch(target, arr): 
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid].country:
            return mid
        elif target > arr[mid].country:
            left = mid + 1
        elif target < arr[mid].country:
            right = mid - 1

    return -1 

arr = readFile()
target = input("Country: ")
pos = binSearch(target, arr)

if pos > 0: 
    print("Capital is: ", arr[pos].capital)
elif pos < 0:
    print("Not found")