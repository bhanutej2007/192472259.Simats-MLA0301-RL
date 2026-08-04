

actions = ["Forward", "Left", "Right"]
scores = [80, 92, 86]

print("Action\tScore")

for i in range(len(actions)):
    print(actions[i], "\t", scores[i])

best = max(scores)
index = scores.index(best)

print("\nOptimal Action :", actions[index])
print("Score :", best)