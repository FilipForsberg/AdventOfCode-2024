

def calculateDifference(leftList, rightList):
    distance = 0
    for values in zip(leftList, rightList):
        distance += abs(values[0] - values[1])
    return distance

def calculateSimilarity(leftList, rightList):
    similarity = 0
    for value in leftList:
        similarity += value * rightList.count(value)
    return similarity

if __name__ == '__main__':
    with open("../Inputs/Day1/input.txt") as input:
        leftList = []
        rightList = []
        for line in input:
            left, right = line.split()
            leftList.append(int(left))
            rightList.append(int(right))
        leftList.sort()
        rightList.sort()

        print(calculateDifference(leftList,rightList))
        print(calculateSimilarity(leftList,rightList))

