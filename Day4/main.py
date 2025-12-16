def split_input(input_string):
    rules = []
    updates = []

    for line in input_string.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if '|' in line:
            rules.append(list(map(int, line.split('|'))))
        elif ',' in line:
            updates.append(list(map(int, line.split(','))))
        else:
            pass

    return rules, updates

def orderUpdates(updates, rules):
    ordered = []
    for update in updates:
        s = set(update)
        graph = {p: [] for p in update}
        indegree = {p: 0 for p in update}
        for a, b in rules:
            if a in s and b in s:
                graph[a].append(b)
                indegree[b] += 1

        queue = [p for p in update if indegree[p] == 0]

        result = []

        while queue:
            node = queue.pop(0)  # pop from front
            result.append(node)

            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        ordered.append(result)
    return(ordered)

def countMiddle(updates):
    total = 0
    for update in updates:
        length = len(update)
        middleIndex = length // 2
        total += update[middleIndex]
    return total

def validateUpdates(updates, rules):
    validUpdate = []
    invalidUpdate = []
    for update in updates:
        valid = True
        for rule in rules:
            a = rule[0]
            b = rule[1]
            if a in update and b in update:
                if update.index(a) > update.index(b):
                    valid = False
                    invalidUpdate.append(update)
                    break
        if valid:
            validUpdate.append(update)
    return validUpdate, invalidUpdate

if __name__ == '__main__':
    example = open("../Inputs/Day4/example.txt.txt").read()
    part1_input = open("../Inputs/Day4/input.txt.txt").read()
    rules,updates = split_input(part1_input)
    valid, invalid = validateUpdates(updates, rules)

    print("Part 1: " ,countMiddle(valid))
    fixedUpdates = orderUpdates(invalid,rules)
    print("Part 2: ", countMiddle(fixedUpdates))









