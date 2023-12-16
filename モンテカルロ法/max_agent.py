import numpy as np
from collections import defaultdict
from grid import GridWorld

class max_agent():
    def __init__(self):
        self.gamma=0.9
        self.action_size=4
        self.epsilon=0.1
        self.alpha=0.1
        random_action={0:(1/self.action_size),1:(1/self.action_size),2:(1/self.action_size),3:(1/self.action_size)}
        self.pi=defaultdict(lambda:random_action)
        self.Q=defaultdict(lambda:0)#Q関数
        self.memory =[]

    def get_action(self,state):
        action_probs=self.pi[state]
        actions=list(action_probs.keys())
        probs =list(action_probs.values())
        return np.random.choice(actions,p=probs)
    def add(self,state,action,reward):
        data=(state,action,reward)
        self.memory.append(data)
    def reset(self):
        self.memory.clear()

    def greedy_probs(self,state,action_size=4):#探索のため確率εでランダム行動
        qs=[self.Q[(state,action)] for action in range(action_size)]
        max_action=np.argmax(qs)
        action_probs={action: self.epsilon/action_size for action in range(action_size)}
        action_probs[max_action]+=1-self.epsilon
        return action_probs
    
    def update(self):
        G=0
        for data in reversed(self.memory):
            state,action,reward=data
            G=self.gamma*G+reward
            self.Q[(state,action)]+=(G-self.Q[(state,action)])*self.alpha
            self.pi[state]=self.greedy_probs(state)

    def show_Q(self,env):
        for state in env.states():
            for action in range(self.action_size):
                print("state "+str(state)+" "+env.action_meaning[action]+" "+str(self.Q[(state,action)]))





