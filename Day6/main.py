
def convertTextTo2dArray(text):
    array = []
    row = []

    for line in text:
        line = line.strip()
        for char in line:
            row.append(char)
        array.append(row)
        row = []

    return array

def findStartPos(array):
    for y, row in enumerate(array):
        for x, col in enumerate(row):
            if col == "^":
                return (y, x)


def findLoop(array, start):
    directions = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1)
    }
    turn_right = {
        "up": "right",
        "right": "down",
        "down": "left",
        "left": "up"
    }

    y, x = start
    facing = "up"
    visited = {((y, x), facing)}
    rows, cols = len(array), len(array[0])

    while True:
        dy, dx = directions[facing]
        newY = y + dy
        newX = x +dx

        if not (0 <= newY < rows and 0 <= newX < cols):
            return False

        if array[newY][newX] != "#":
            y, x = newY, newX
            pos = ((y, x), facing)
            if pos in visited:
                return True
            visited.add(pos)
        else:
            facing = turn_right[facing]

def findPath(array, start):
    directions = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1)
    }
    turn_right = {
        "up": "right",
        "right": "down",
        "down": "left",
        "left": "up"
    }

    y, x = start
    facing = "up"
    visited = {(y, x)}
    rows, cols = len(array), len(array[0])

    while True:
        dy, dx = directions[facing]
        newY = y + dy
        newX = x + dx

        if not (0 <= newY < rows and 0 <= newX < cols):
            break

        if array[newY][newX] != "#":
            y, x = newY, newX
            visited.add((y, x))
        else:
            facing = turn_right[facing]

    return visited

if __name__ == '__main__':
    example = open("../Inputs/Day6/example.txt").readlines()
    input = open("../Inputs/Day6/input.txt").readlines()

    array = convertTextTo2dArray(input)
    startPosition = findStartPos(array)
    guardPathSet = findPath(array, startPosition)

    print("Part 1: " ,len(guardPathSet))

    loops = 0
    for point in guardPathSet:
        (y,x) = point
        array[y][x] = "#"
        if (findLoop(array, startPosition)):
            loops += 1
        array[y][x] = "."
    print("Part 2: ", loops)


