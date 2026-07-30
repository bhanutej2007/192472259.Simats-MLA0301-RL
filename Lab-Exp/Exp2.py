# Experiment 2: Smart Home Robot

actions = ["Move Left", "Move Right", "Move Forward"]
rewards = [2, 3, 5]

print("Smart Home Navigation")
print("1.Move Left")
print("2.Move Right")
print("3.Move Forward")

choice = int(input("Enter your choice: "))

if 1 <= choice <= 3:
    print("Selected Action :", actions[choice-1])
    print("Reward :", rewards[choice-1])
    print("Navigation Successful")
else:
    print("Invalid Choice")