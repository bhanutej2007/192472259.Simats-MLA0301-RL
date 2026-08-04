

signals = ["North", "South", "East", "West"]
scores = [25, 18, 30, 20]

print("Signal\tScore")

for i in range(len(signals)):
    print(signals[i], "\t", scores[i])

best = max(scores)
index = scores.index(best)

print("\nGreen Signal :", signals[index])
print("Score :", best)