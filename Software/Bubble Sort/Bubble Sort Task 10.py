def readfile():
    with open("baseball.txt", "r") as file:
        team = []
        wsWins = []
        stadium = []
        capacity = []

        for line in file.readlines():
            line = line.split(",")

            team.append(line[0])
            wsWins.append(int(line[1]))
            stadium.append(line[2])
            capacity.append(int(line[3]))


    return team,wsWins,stadium,capacity

team,wsWins,stadium,capacity = readfile()

def display(x, y):
    for i in range(len(x)):
        print(x[i], y[i])
    

def sortStadiums(stadium, capacity):
    swapped = True
    length = len(capacity)

    while length >= 0 and swapped:
        swapped = False
        for i in range(length-1):
            if capacity[i] < capacity[i+1]:
                capacity[i], capacity[i+1] = capacity[i+1], capacity[i]
                stadium[i], stadium[i+1] = stadium[i+1], stadium[i]
                swapped = True
        length -= 1

    print("sort stadium \n")
    display(stadium, capacity)



def sortWorldSeriesWins(team, wsWins):
    swapped = True
    length = len(capacity)

    while length >= 0 and swapped:
        swapped = False
        for i in range(length-1):
            if wsWins[i] < wsWins[i+1]:
                wsWins[i], wsWins[i+1] = wsWins[i+1], wsWins[i]
                team[i], team[i+1] = team[i+1], team[i]
                swapped = True
        length -= 1

    print("sort ws \n")
    display(team, wsWins)

sortStadiums(stadium, capacity)
sortWorldSeriesWins(team, wsWins)