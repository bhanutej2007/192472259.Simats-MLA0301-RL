

strategies = ["Low Stock", "Medium Stock", "High Stock"]
rewards = [50, 80, 65]

print("Strategy\tReward")

for i in range(len(strategies)):
    print(strategies[i], "\t", rewards[i])

best = max(rewards)
index = rewards.index(best)

print("\nBest Strategy :", strategies[index])
print("Reward :", best)