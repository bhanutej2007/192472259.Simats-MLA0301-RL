

observations = ["Obstacle", "Clear Path", "Unknown"]
actions = ["Stop", "Move", "Scan"]

for i in range(len(observations)):
    print("Observation :", observations[i])
    print("Action :", actions[i])
    print("Reward :", (i + 1) * 5)
    print()