

actions = ["Buy", "Hold", "Sell"]
profits = [1200, 800, 1500]

print("Action\tProfit")

for i in range(len(actions)):
    print(actions[i], "\t", profits[i])

best = max(profits)
index = profits.index(best)

print("\nBest Action :", actions[index])
print("Profit :", best)