from grid import GridWorld
from collections import defaultdict
#ランダムに動くエージェントを対象とした状態価値を求めるプログラム
def one_step(pi,V,env,gamma=0.9):
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
    return V
def policy_eval(pi,V,env,gamma,threshould=0.001):
    while True:
        old_V=V.copy()
        V=one_step(pi,V,env,gamma)
        delta=0
        for state in env.states():
            t=abs(old_V[state]-V[state])
            if delta<t:
                delta=t
        if delta < threshould:
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
print(V[(0,0)])
V=policy_eval(pi,V,env,0.9)
show_val(V)

