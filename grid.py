import numpy as np
class GridWorld:
    def __init__(self):
        self.action_space ={0,1,2,3}
        self.action_meaning={
            0:"UP",
            1:"DOWN",
            2:"LEFT",
            3:"RIGHT",
        }
        self.reward_map =np.array(
            [[0,0,0,1.0],
             [0,None,0,-1.0],
             [0,0,0,0]]
        )
        self.goal_state=(0,3)
        self.wall_state=(1,1)
        self.start_state=(2,0)
        self.agent_state=self.start_state

    @property
    def height(self):
        return len(self.reward_map)
    @property
    def width(self):
        return len(self.reward_map[0])
    @property
    def shape(self):
        return self.reward_map.shape
    @property
    def actions(self):
        return self.action_space
        
    def states(self):
        for h in range(self.height):
            for w in range(self.width):
                yield (h,w)
        
    def next_state(self,action,state):
        action_move_map=[(-1,0),(1,0),(0,-1),(0,1)]
        move=action_move_map[action]
        next_state=(state[0]+move[0],state[1]+move[1])
        if next_state[0]<0 or next_state[0] >= self.height or next_state[1]<0 or next_state[1]>=self.width :
            return state
        elif next_state==self.wall_state:
            return state
        return next_state
    def reward(self,state,action,next_state):
        return self.reward_map[next_state]
        
                



            
