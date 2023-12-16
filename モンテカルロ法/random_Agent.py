import numpy as np
from collections import defaultdict

class ramdom_agent():
    def __init__(self):
        self.gamma=0.9
        self.action_size=4
        random_action={0:(1/self.action_size),1:(1/self.action_size),2:(1/self.action_size),3:(1/self.action_size)}
        self.pi=defaultdict(lambda:random_action)
        self.V=defaultdict(lambda:0)
        self.cnts=defaultdict(lambda :0)
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
    
    def eval(self):
        G=0
        for data in reversed(self.memory):
            state,action,reward=data
            G=self.gamma*G+reward
            self.cnts[state]+=1
            self.V[state]+=(G-self.V[state])/self.cnts[state]

