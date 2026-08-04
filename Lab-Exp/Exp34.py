
temperature = ["22°C", "24°C", "26°C"]
comfort = [85, 95, 80]

print("Temperature\tComfort")

for i in range(len(temperature)):
    print(temperature[i], "\t\t", comfort[i])

best = max(comfort)
index = comfort.index(best)

print("\nBest Temperature :", temperature[index])
print("Comfort Score :", best)