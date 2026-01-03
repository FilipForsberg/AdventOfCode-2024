import re


def find_vertical(input):
    lines = [line.strip() for line in input.splitlines()]

    lineLength = len(lines[0])
    numberOfLines = len(lines)
    rotated = ""
    for j in range(lineLength):
        for i in range(numberOfLines):
            row = lines[i]
            rotated += row[j]
        rotated += "\n"
    pattern = r"(?=(XMAS|SAMX))"
    matches = [m.group(1) for m in re.finditer(pattern, rotated)]

    return len(matches)

def find_diagonal(input):

    lines = [line.strip() for line in input.splitlines()]
    cols = len(lines[0])
    rows = len(lines)
    diagList = []
    diag = ""
    #Top-Left -> Bottom-Right (Top Right half)
    for j in range(cols):
        substring = ""
        currentRow, currentCol = 0, j
        while currentRow < rows and currentCol < cols:
            line = lines[currentRow]
            substring += line[currentCol]
            currentRow += 1
            currentCol += 1

        diagList.append(substring)
    #Top-Left -> Bottom-Right (Bottom-Left half)
    for i in range(1, rows):
        substring = ""
        currentRow = i;
        currentCol = 0
        while currentRow < rows and currentCol < cols:
            line = lines[currentRow]
            substring += line[currentCol]
            currentRow += 1
            currentCol += 1
        diagList.append(substring)

    #Top-Right to Bottom-Left (Top-Left Half)
    for j in range(1, cols):
        substring = ""
        currentRow = 0
        currentCol = cols - j
        while currentRow < rows and currentCol > -1:
            line = lines[currentRow]
            substring += line[currentCol]
            currentRow += 1
            currentCol -= 1
        diagList.append(substring)

    #Top-Right to Bottom-Left (Bottom-Right Half)
    for i in range(1,rows):
        substring = ""
        currentRow = i
        currentCol = cols - 1
        while currentRow < rows and currentCol > -1:
            line = lines[currentRow]
            substring += line[currentCol]
            currentRow += 1
            currentCol -= 1
        diagList.append(substring)

    count = 0
    pattern = r"(?=(XMAS|SAMX))"
    for diagonal in diagList:
        if len(diagonal) >= 4:
            count += len(re.findall(pattern, diagonal))

    return count


def find_horizontal(input):
    pattern = r"(?=(XMAS|SAMX))"
    matches = [m.group(1) for m in re.finditer(pattern, input)]

    return len(matches)

def solve_part_1(input):
    return 0



if __name__ == '__main__':
    example = open("../Inputs/Day4/example.txt").read()
    input = open("../Inputs/Day4/input.txt").read()
    test = open("../Inputs/Day4/test.txt").read()

    horizontal = find_horizontal(input)
    vertical = find_vertical(input)
    diagonal = find_diagonal(input)
    print(horizontal, vertical, diagonal)
    total = horizontal + vertical + diagonal
    print(total)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



