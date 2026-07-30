# Experiment 9: TD(0), SARSA and Q-Learning

reward = 5
alpha = 0.5
gamma = 0.9
q = 2
next_q = 4

td = reward + gamma * next_q
sarsa = q + alpha * (td - q)
qlearning = q + alpha * (reward + gamma * max(next_q, q) - q)

print("TD Value:", td)
print("SARSA Value:", round(sarsa,2))
print("Q-Learning Value:", round(qlearning,2))