

actions = ["Move", "Jump", "Block"]
q_values = [10, 18, 15]

print("Action\tQ-Value")

for i in range(len(actions)):
    print(actions[i], "\t", q_values[i])

best = max(q_values)
index = q_values.index(best)

print("\nBest Action :", actions[index])
print("Q-Value :", best)