import numpy as np
from collections import defaultdict
from grid import GridWorld

class TD_agent():
    def __init__(self):
        self.gamma=0.9
        self.alpha=0.01
        self.action_size=4
        self.V=defaultdict(lambda:0)
        random_action={0:(1/self.action_size),1:(1/self.action_size),2:(1/self.action_size),3:(1/self.action_size)}
        self.pi=defaultdict(lambda:random_action)


    def get_action(self,state):
        action_prob=self.pi[state]
        actions=list(action_prob.keys())
        probs=list(action_prob.values())
        return np.random.choice(actions,p=probs)
    
    def eval(self,state,reward,nextstate,done):
        next_V= 0 if done else self.V[nextstate] 
        self.V[state]+=self.alpha*(reward+self.gamma*next_V-self.V[state])

    def show(self,env):
        for state in env.states():
            print(str(state)+" "+str(self.V[state]))
    




