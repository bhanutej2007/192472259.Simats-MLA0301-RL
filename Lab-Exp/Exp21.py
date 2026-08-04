

treatments = ["Medicine A", "Medicine B", "Surgery"]
rewards = [75, 90, 85]

print("Treatment\tReward")

for i in range(len(treatments)):
    print(treatments[i], "\t", rewards[i])

best = max(rewards)
index = rewards.index(best)

print("\nBest Treatment :", treatments[index])
print("Reward :", best)