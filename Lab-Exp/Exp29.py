

servers = ["Server A", "Server B", "Server C"]
usage = [65, 90, 75]

print("Server\tUsage")

for i in range(len(servers)):
    print(servers[i], "\t", usage[i])

best = max(usage)
index = usage.index(best)

print("\nSelected Server :", servers[index])
print("Usage :", best)