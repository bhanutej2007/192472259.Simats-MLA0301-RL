# Experiment 3: Warehouse Robot MDP

states = ["Entrance", "Shelf", "Packing", "Exit"]
actions = ["Move", "Pick Item", "Deliver"]
reward = [0, 4, 8, 10]

for i in range(len(states)):
    print("State :", states[i])

    if i < len(actions):
        print("Action :", actions[i])

    print("Reward :", reward[i])
    print("----------------")