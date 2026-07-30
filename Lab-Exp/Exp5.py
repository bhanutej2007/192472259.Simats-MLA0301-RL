import random

ads = ["Ad A", "Ad B", "Ad C"]
epsilon = 0.3

r = random.random()

if r < epsilon:
    ad = random.choice(ads)
    print("Exploration")
else:
    ad = ads[0]
    print("Exploitation")

print("Selected Advertisement :", ad)