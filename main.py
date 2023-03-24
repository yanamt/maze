import numpy as np
import matplotlib.pyplot as plt
from agent import Agent
from world import World
import pdb

# パラメータ
num_episode = 100
Epsilon = .1
Alpha = .1
Gamma = .9
Actions = np.arange(4)
size = 10

if __name__ == "__main__":
    env = World()
    ini_state = env.start_pos

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
        print(episode)
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
