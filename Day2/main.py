
def is_valid(values):
    safe_diffs = {1,2,3}
    trend = None
    for i in range(len(values) - 1):
        a = values[i]
        b = values[i + 1]
        difference = a - b
        absDifference = abs(a -b)

        if(absDifference not in safe_diffs):
            return (False, i)

        if difference < 0:
            step_trend = "increasing"
        else:
            step_trend = "decreasing"

        if trend is None:
            trend = step_trend
        elif step_trend != trend:
            return (False, i)
    return True, i

def is_valid_with_one_removal(values):
    valid, index = is_valid(values)
    if valid:
        return True

    v1 = values[:index] + values[index + 1:]
    valid, a = is_valid(v1)
    if valid:
        return True

    v2 = values[:index + 1] + values[index + 2:]
    valid, b = is_valid(v2)
    if valid:
        return True
    return False

if __name__ == '__main__':
    with open("../Inputs/Day2/input.txt") as f:
        input = f.readlines()
    part_1_numberSafe = 0
    part_2_numberSafe = 0
    for line in input:
        values = [int(x) for x in line.strip().split()]   # convert to ints immediately
        ### Part One ###
        p1_safe, index = is_valid(values)
        if p1_safe:
            part_1_numberSafe += 1
        ### Part Two ###
        p2_safe = is_valid_with_one_removal(values)
        if p2_safe:
            part_2_numberSafe += 1


    print("Part 1 Number safe:", part_1_numberSafe)
    print("Part 2 Number safe:", part_2_numberSafe)




