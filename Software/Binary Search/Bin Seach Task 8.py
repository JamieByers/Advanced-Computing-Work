rows = 233
cols = 5

def readFile():
    array = [[None]*cols for index in range(rows)] 
    with open("golf.csv", "r") as file:
        r = 0 
        line = file.readline().rstrip("\n")
        while line: 
            items = line.split(",")
            for c in range(cols):
                array[r][c] = items[c]
            r += 1
            line = file.readline().rstrip("\n")
   
    return array

arr = readFile()

def binSearch(target, arr): 
    left = 0 
    right = len(arr)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid][0] == target:
            return mid
        elif arr[mid][0] < target:
            left = mid + 1
        elif arr[mid][0] > target:
            right = mid - 1

    return -1

print(binSearch("Justin Rose", arr))