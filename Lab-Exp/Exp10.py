# Experiment 10: Simple DQN

actions = ["Left", "Right", "Forward"]
q_values = [2.5, 4.8, 3.6]

print("Actions:", actions)
print("Q-Values:", q_values)

best = max(q_values)
index = q_values.index(best)

print("Best Action:", actions[index])
print("Maximum Q-Value:", best)