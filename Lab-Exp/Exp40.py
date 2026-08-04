

activities = ["Video Lecture", "Quiz", "Coding Practice"]
reward = [70, 82, 96]

print("Learning Recommendation\n")

for i in range(len(activities)):
    print(activities[i], "Reward:", reward[i])

best = max(reward)
index = reward.index(best)

print("\nRecommended Activity :", activities[index])
print("Reward :", best)