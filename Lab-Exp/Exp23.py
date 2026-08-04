

methods = ["Video", "Quiz", "Practice"]
rewards = [70, 80, 95]

print("Method\tReward")

for i in range(len(methods)):
    print(methods[i], "\t", rewards[i])

best = max(rewards)
index = rewards.index(best)

print("\nBest Method :", methods[index])
print("Reward :", best)