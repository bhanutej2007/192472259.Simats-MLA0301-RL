# Experiment 15: PPO

paths = ["Path A", "Path B", "Path C"]
rewards = [15, 20, 18]

print("Available Paths")

for i in range(len(paths)):
    print(paths[i], ":", rewards[i])

best = max(rewards)
index = rewards.index(best)

print("\nBest Path:", paths[index])
print("Reward:", best)