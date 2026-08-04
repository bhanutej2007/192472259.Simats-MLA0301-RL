
portfolio = ["Portfolio A", "Portfolio B", "Portfolio C"]
value = [120, 150, 135]

print("Portfolio\tValue")

for i in range(len(portfolio)):
    print(portfolio[i], "\t", value[i])

best = max(value)
index = value.index(best)

print("\nBest Portfolio :", portfolio[index])
print("Predicted Value :", best)