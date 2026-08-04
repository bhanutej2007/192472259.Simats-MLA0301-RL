

robots = ["Robot A", "Robot B", "Robot C"]
rewards = [20, 25, 18]

print("Robot\t\tReward")

for i in range(len(robots)):
    print(robots[i], "\t", rewards[i])

best = max(rewards)
index = rewards.index(best)

print("\nBest Robot :", robots[index])
print("Reward :", best)