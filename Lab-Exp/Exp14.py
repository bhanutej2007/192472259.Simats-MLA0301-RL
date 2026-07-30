# Experiment 14: Actor-Critic

actions = ["Accelerate", "Brake", "Turn"]
rewards = [8, 4, 10]

print("Actions and Rewards")

for i in range(len(actions)):
    print(actions[i], ":", rewards[i])

best = max(rewards)
index = rewards.index(best)

print("\nBest Action:", actions[index])
print("Reward:", best)