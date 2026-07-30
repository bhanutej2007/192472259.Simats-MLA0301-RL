# Experiment 12: Policy-Based RL

actions = ["Left", "Right", "Forward"]
probability = [0.2, 0.3, 0.5]

print("Available Actions:")
for i in range(len(actions)):
    print(actions[i], ":", probability[i])

best = max(probability)
index = probability.index(best)

print("\nSelected Action:", actions[index])
print("Probability:", best)