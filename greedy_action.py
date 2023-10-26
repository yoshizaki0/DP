from grid import GridWorld
from collections import defaultdict
def argmax(d):
   max_value=max(d.values())
   max_key=0
   for key,value in d.items():
      if value == max_value:
         max_key=key
   return max_key
      

def pi_eval(pi,V,env,gamma):
   for state in env.states():
        action_value={0:0,1:0,2:0,3:0}
        for action in env.action_space:
            next_state=env.next_state(action,state)
            r=env.reward(state,action,next_state)
            action_value[action]=r+gamma*V[next_state]
        best_action=argmax(action_value)
        action_prob={0:0,1:0,2:0,3:0}
        action_prob[best_action]=1.0
        pi[state]=action_prob
   return pi
def V_eva(pi,V,env,gamma=0.9):
    while True:
        old_V=V.copy()
        for state in env.states():
            if env.goal_state==state:
                V[state]=0
                continue

            action_probs=pi[state]
            new_V=0
            for action,prob in action_probs.items():
                next_state=env.next_state(action,state)
                r=env.reward(state,action,next_state)
                new_V+=prob*(r+gamma*V[next_state])
            V[state]=new_V
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
pi=defaultdict(lambda:{0:0.25, 1:0.25, 2:0.25, 3:0.25})
env=GridWorld()
while True:
   V=V_eva(pi,V,env)
   old_pi=pi.copy()
   pi=pi_eval(pi,V,env,0.9)
   if pi==old_pi:
       break
   
show_val(V)
