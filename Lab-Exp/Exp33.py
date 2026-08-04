
strategies = ["Collect", "Attack", "Build"]
rewards = [45, 60, 55]

print("Strategy\tReward")

for i in range(len(strategies)):
    print(strategies[i], "\t", rewards[i])

best = max(rewards)
index = rewards.index(best)

print("\nBest Strategy :", strategies[index])
print("Reward :", best)