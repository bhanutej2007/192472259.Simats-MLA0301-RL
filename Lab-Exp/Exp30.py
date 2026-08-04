
actions = ["Attack", "Defend", "Hide"]
scores = [75, 60, 90]

print("Action\tScore")

for i in range(len(actions)):
    print(actions[i], "\t", scores[i])

best = max(scores)
index = scores.index(best)

print("\nBest Action :", actions[index])
print("Score :", best)