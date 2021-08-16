"""

    Simple script to check gym is correctly installed and its output is being correctly
    re-directed to the appropriate display.

"""
import time
import gym
import matplotlib.pyplot as plt


if __name__ == "__main__":
    env = gym.make("MountainCar-v0")

    obs = env.reset()

    for _ in range(500):
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)

        env.render(mode="human")
        time.sleep(0.001)
    env.close()
