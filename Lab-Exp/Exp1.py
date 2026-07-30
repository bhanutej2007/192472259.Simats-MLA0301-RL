# Experiment 1: MDP for Simplified Chess Game

states = ["Start", "Middle", "Goal"]
actions = ["Knight Move", "Queen Move"]
rewards = [0, 5, 10]

current = 0

print("Simplified Chess Game using MDP\n")

while current < len(states):
    print("Current State :", states[current])

    if current < len(actions):
        print("Action Taken  :", actions[current])

    print("Reward         :", rewards[current])
    print("-------------------------")

    current += 1

print("Goal State Reached")