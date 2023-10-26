from grid import GridWorld
from collections import defaultdict

def V_eva(V,env,gamma=0.9):
    while True:
        old_V=V.copy()
        for state in env.states():
            if env.goal_state==state:
                V[state]=0
                continue

            temp_V={0:0,1:0,2:0,3:0}
            for action in env.action_space:
                next_state=env.next_state(action,state)
                r=env.reward(state,action,next_state)
                temp_V[action]=r+gamma*V[next_state]
                
            V[state]=max(temp_V.values())
        delta=0
        for state in env.states():
            t=abs(old_V[state]-V[state])
            if delta<t:
                delta=t
        if delta < 0.001:
            break
    return V


def show_val(V):
    print("(0,0) "+str(V[(0,0)]))
    print("(0,1) "+str(V[(0,1)]))
    print("(0,2) "+str(V[(0,2)]))
    print("(0,3) "+str(V[(0,3)]))
    print("(1,0) "+str(V[(1,0)]))
    print("(1,1) "+str(V[(1,1)]))
    print("(1,2) "+str(V[(1,2)]))
    print("(1,3) "+str(V[(1,3)]))
    print("(2,0) "+str(V[(2,0)]))
    print("(2,1) "+str(V[(2,1)]))
    print("(2,2) "+str(V[(2,2)]))
    print("(2,3) "+str(V[(2,3)]))
V=defaultdict(lambda: 0)
env=GridWorld()
V=V_eva(V,env)
show_val(V)

