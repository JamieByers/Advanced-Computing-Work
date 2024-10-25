class PlayerRecord:
    name = ""
    points = 0
    games = 0
    ppg = 0.0

def readFile():
    arr = []
    with open("basketball.csv", "r") as file:
        for line in file.readlines():
            line = line.split(",")

            player = PlayerRecord()

            player.name = line[0]
            player.points = int(line[1])
            player.games = int(line[2])

            arr.append(player)

    return arr

def calculateAverage(players):
    for player in players:
        player.ppg = player.points / player.games
    return players

def printData(arr):
    for p in arr:
        print(p.name, p.points, p.games, p.ppg)

    print()

def sortAverage(players):
    swapped = True
    length = len(players)

    while length >= 0 and swapped:
        swapped = False
        for i in range(length-1):
            if players[i].ppg < players[i+1].ppg:
                players[i], players[i+1] = players[i+1], players[i]
                swapped = True
        length -= 1

    print("PPG")
    printData(players)
    return players

def sortPoints(players):
    swapped = True
    length = len(players)

    while length >= 0 and swapped:
        swapped = False
        for i in range(length-1):
            if players[i].points < players[i+1].points:
                players[i], players[i+1] = players[i+1], players[i]
                swapped = True
        length -= 1

    print("POINTS")
    printData(players)
    return players


arr = readFile()
arr = calculateAverage(arr)
sortAverage(arr)
sortPoints(arr)

