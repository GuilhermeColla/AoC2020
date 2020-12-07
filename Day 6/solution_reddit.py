# Credits to u/Ody55eu5_ for the solution
# Comment link: https://www.reddit.com/r/adventofcode/comments/k7ndux/2020_day_06_solutions/gevut6v?utm_source=share&utm_medium=web2x&context=3

example = 1
if example:
    with open('Day 6/example_input', 'r') as f:
        origData = f.read()
else:
    with open('Day 6/puzzle_input', 'r') as f:
        origData = f.read()
    
allData = origData.split('\n\n')

print("Part 1:",sum([len(set(d.replace('\n',''))) for d in allData]))

print("Part 2:", sum([len(set.intersection(*[set(item) for item in groupData])) for groupData in [d.split('\n') for d in allData]]))
