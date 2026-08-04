
paths = ["Path A", "Path B", "Path C"]
cost = [18, 10, 15]

print("Path\tCost")

for i in range(len(paths)):
    print(paths[i], "\t", cost[i])

best = min(cost)
index = cost.index(best)

print("\nShortest Path :", paths[index])
print("Cost :", best)