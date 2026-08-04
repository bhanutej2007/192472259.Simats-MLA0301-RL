

actions = ["Go Straight", "Turn Left", "Turn Right", "Brake"]
rewards = [20, 15, 18, 25]

print("Action\t\tReward")

for i in range(len(actions)):
    print(actions[i], "\t", rewards[i])

best = max(rewards)
index = rewards.index(best)

print("\nBest Action :", actions[index])
print("Reward :", best)