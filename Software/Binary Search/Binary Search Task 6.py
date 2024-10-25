def readFile():
    city = []
    country = []
    year = []
    with open("olympics.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.split(",")
            city.append(line[0])
            country.append(line[1])
            year.append(int(line[2]))

    return city, country, year

city, country, year = readFile()

# print(city, country, year )

target = int(input("Input year: "))

def binSearch(city, country, year, target): 
    left = 0
    right = len(year)-1

    while left <= right:
        mid = (left + right) // 2

        if target == year[mid]:
            print(f"The {year[mid]} summer olympics were held in {city[mid]}, {country[mid]}")
            return mid
        elif target > year[mid]:
            left = mid + 1
        elif target < year[mid]:
            right = mid - 1

    print("Not found")
    return -1 

binSearch(city, country, year, target)