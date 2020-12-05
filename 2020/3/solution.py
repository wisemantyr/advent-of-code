import math

with open('input.txt', 'r') as f:
    inp = [line.strip() for line in f]
room = len(inp[0]) - 1
rows = len(inp)
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

trees = []
for (right, down) in slopes:
    tree_count = 0
    moves = math.floor(room/right)
    iters = round((rows - down)/moves)
    repeated = [(line*iters) for line in inp]
    forest = repeated[down::down]
    index = right
    for row in forest:
        if row[index] == "#":
            tree_count = tree_count + 1
        index += right
    trees.append(tree_count)
solution = math.prod(trees)
print(solution)