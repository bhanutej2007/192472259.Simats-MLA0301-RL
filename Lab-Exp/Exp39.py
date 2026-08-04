

responses = ["Welcome!", "How can I help?", "Thank You!"]
reward = [60, 95, 75]

print("Customer Support Chatbot\n")

for i in range(len(responses)):
    print(responses[i], "Reward:", reward[i])

best = max(reward)
index = reward.index(best)

print("\nBest Response :", responses[index])
print("Reward :", best)