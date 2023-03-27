import numpy as np
import matplotlib.pyplot as plt
from agent import Agent
from world import World
from generator import Generator

# パラメータ
num_episode = 300
Epsilon = .1
Alpha = .1
Gamma = .9
Actions = np.arange(4)
size = 10

if __name__ == "__main__":
    output = Generator(size)
    _, maze_map, step = output.generate()
    for line in maze_map:
        print(line)
    print(step)
    ini_state = 0, size-1
    env = World(ini_state, maze_map)

    # エージェントの初期化
    agent = Agent(
        alpha=Alpha,
        gamma=Gamma,
        epsilon=Epsilon,
        actions=Actions,
        observation=ini_state
    )
    rewards = []
    is_end_episode = False

    for episode in range(num_episode):
        episode_reward = []
        while(is_end_episode == False):
            action = agent.act()
            state, reward, is_end_episode = env.step(action)
            agent.observe(state, reward)
            episode_reward.append(reward)
        rewards.append(np.sum(episode_reward))
        state = env.reset()
        agent.observe(state)
        is_end_episode = False
        # 結果のプロット
    plt.plot(np.arange(num_episode), rewards)
    plt.xlabel("episode")
    plt.ylabel("reward")
    plt.savefig("result.jpg")
    plt.show()
