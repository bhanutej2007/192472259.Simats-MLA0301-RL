

sources = ["Solar", "Wind", "Hydro"]
efficiency = [88, 82, 91]

print("Source\tEfficiency")

for i in range(len(sources)):
    print(sources[i], "\t", efficiency[i])

best = max(efficiency)
index = efficiency.index(best)

print("\nBest Source :", sources[index])
print("Efficiency :", best)