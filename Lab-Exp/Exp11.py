# Experiment 11: Comparison of DQN Variants

algorithms = ["DQN", "DDQN", "Dueling DQN", "PER"]
q_values = [6.5, 7.2, 7.8, 8.1]

for i in range(len(algorithms)):
    print(algorithms[i], ":", q_values[i])

best = max(q_values)
index = q_values.index(best)

print("\nBest Algorithm:", algorithms[index])
print("Best Q-Value:", best)