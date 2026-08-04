

tasks = ["Search", "Pick", "Deliver"]
rewards = [10, 15, 20]

total = 0

for i in range(len(tasks)):
    print(tasks[i], "Reward :", rewards[i])
    total += rewards[i]

print("\nTotal Reward :", total)