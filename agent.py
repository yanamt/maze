import copy
import numpy as np

class Agent:
    #学習を行うエージェント
    def __init__(
        self,
        alpha=.2,
        epsilon=.1,
        gamma=.99,
        actions=None,
        observation=None
        ):
        self.alpha=alpha
        self.gamma=gamma
        self.epsilon=epsilon
        self.reward_history=[]
        self.actions=actions
        self.state=str(observation)
        self.ini_state=str(observation)
        self.previous_state=None
        self.previous_action=None
        self.q_values=self._init_q_values()
    
    def _init_q_values(self):
        #Qテーブルの初期化
        q_values=[]
        q_values[self.state]=np.repeat(0.0,len(self.actions))
        return q_values
    
    def init_state(self):
        #状態の初期化
        self.previous_state=copy.deepcopy(self.ini_state)
        self.state=copy.deepcopy(self.ini_state)
        return self.state
    
    def act(self):
        #ε-greedy行動選択
        if np.random.uniform()<self.epsilon:
            action=np.random.randint(0,len(self.q_values[self.state]))
        else:
            action=np.argmax(self.q_values[self.state])
            
        self.previous_action=action
        return action
    
    def observe(self,next_state,reward=None):
        #次の状態と報酬を観測する
        
        next_state=str(next_state)
        if next_state not in self.q_values:
            self.q_values[next_state]=np.repeat(0.0,len(self.actions))
        
        self.previous_state=copy.deepcopy(self.state)
        self.state=next_state
        
        if reward is not None:
            self.reward_history.append(reward)
            self.learn(reward)
            
    def learn(self,reward):
        #Q値の更新を行う
        
        q=self.q_values[self.previous_state][self.previous_action]
        max_q=max(self.q_values[self.state])
        #Q(s,a)<-Q(s,a)+alpha*(r+gamma*maxQ(s')-Q(s,a))
        self.q_values[self.previous_state][self.previous_action]=q+(self.alpha*(reward+(self.gamma*max_q)-q))