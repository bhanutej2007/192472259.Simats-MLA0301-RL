
paths = ["Path A", "Path B", "Path C"]
scores = [82, 95, 88]

print("Drone Navigation\n")

for i in range(len(paths)):
    print(paths[i], "Score:", scores[i])

best = max(scores)
index = scores.index(best)

print("\nBest Path :", paths[index])
print("Navigation Score :", best)