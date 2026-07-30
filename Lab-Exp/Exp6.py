import gymnasium as gym

env = gym.make("CartPole-v1")

state, info = env.reset()

print("Initial State:")
print(state)

action = env.action_space.sample()

state, reward, terminated, truncated, info = env.step(action)

print("Action :", action)
print("Reward :", reward)

env.close()