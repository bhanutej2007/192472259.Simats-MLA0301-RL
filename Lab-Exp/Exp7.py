# Experiment 7: Dynamic Programming

rewards = [5, 8, 10]
gamma = 0.9

values = []

for reward in rewards:
    values.append(reward * gamma)

print("Updated Route Values")

for i in range(len(values)):
    print("Route", i + 1, ":", values[i])