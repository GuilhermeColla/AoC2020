
myFile = open("Day 7/puzzle_input", "r")
content = myFile.read().splitlines()

def part1(bags, stringNeeded):
    bagsList = []
    for x in bags:
        findBag = x.find(' bags contain')
        if stringNeeded in x[findBag:]:
            bagsList.append(x[:findBag])
            bagsList.extend(part1(bags, x[:findBag]))
    return bagsList

print(len(set(part1(content, "shiny gold"))))