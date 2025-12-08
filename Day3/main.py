import re

def solve_part_1(input):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    sum = 0
    for match in matches:
        a = int(match[0])
        b = int(match[1])
        sum += a*b
    return sum

def solve_part_2(input):
    pattern = (
        r"(?P<do>do\(\))"  # do
        + r"|(?P<dont>don't\(\))" # Dont
        + r"|(?P<mul>mul\((?P<a>\d+),(?P<b>\d+)\))"  # multi
    )
    matches = re.finditer(pattern, input)
    sum = 0
    addSumBool = True
    for match in matches:
        dict = match.groupdict()
        if dict['do'] and dict['dont']:
            doIndex = match.start('do')
            dontIndex = match.start('dont')

            addSumBool = doIndex > dontIndex
        elif dict['do']:
            addSumBool = True
        elif dict['dont']:
            addSumBool = False

        if addSumBool and dict['mul']:
            a = int(dict['a'])
            b = int(dict['b'])
            sum += a*b
    return sum

if __name__ == '__main__':
    example = open("../Inputs/Day3/example.txt").read()
    input = open("../Inputs/Day3/input.txt").read()
    example2 = open("../Inputs/Day3/example2.txt").read()

    print(solve_part_1(input))

    print(solve_part_2(input))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
