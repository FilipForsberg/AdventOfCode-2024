def readInput(input):
    inputArray = []

    for line in input:
        sum, numbers = line.split(":")
        numbers = numbers.strip().split()

        numbers = [int(number) for number in numbers]

        inputArray.append((int(sum), numbers))
    return inputArray


def createStates(numbers, value, concat):
    states = {numbers[0]}
    for n in numbers[1:]:
        next_state = set()
        for s in states:
            if s > value:
                continue
            next_state.add(s + n)
            next_state.add(s * n)
            if concat:
                next_state.add(int(f"{s}{n}"))

        states = next_state
    return states



def Solve(inputArray, concat):
    sum = 0
    for row in inputArray:
        value = row[0]
        numbers = row[1]
        states = createStates(numbers, value, concat)
        if value in states:
            sum += value

    return sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    example = open("../Inputs/Day7/example.txt").readlines()
    input = open("../Inputs/Day7/input.txt").readlines()

    exampleArray = readInput(example)
    inputArray = readInput(input)

    print("Part 1: ", Solve(inputArray, False))


    print("Part 2: " , Solve(inputArray, True))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
