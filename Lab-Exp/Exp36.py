
agents = ["Agent A", "Agent B", "Agent C"]
reward = [55, 68, 62]

print("Agent\tReward")

for i in range(len(agents)):
    print(agents[i], "\t", reward[i])

best = max(reward)
index = reward.index(best)

print("\nBest Agent :", agents[index])
print("Reward :", best)