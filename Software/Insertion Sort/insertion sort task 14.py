def readFile():
    country = []
    area = []

    with open("world.csv", "r") as file:
        for line in file.readlines():
            line = line.strip("\n").split(",")

            country.append(line[0])
            area.append(int(line[1]))

    return country, area

country, area = readFile()

def insertionSort(country, area):
    for i in range(1, len(area)):
        value1 = country[i]
        value2 = area[i]
        j = i
        while value2 > area[j-1] and j > 0:
            country[j] = country[j-1] 
            country[j-1] = value1 
            area[j] = area[j-1] 
            area[j-1] = value2
            j -= 1

    return country, area


print(insertionSort(country, area))