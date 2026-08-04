

actions = ["Accelerate", "Brake", "Turn"]
policy = [0.65, 0.90, 0.75]

print("Action\t\tPolicy Score")

for i in range(len(actions)):
    print(actions[i], "\t", policy[i])

best = max(policy)
index = policy.index(best)

print("\nBest Action :", actions[index])
print("Policy Score :", best)