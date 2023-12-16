from grid import GridWorld
from random_Agent import ramdom_agent

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


env=GridWorld()
agent=ramdom_agent()
episodes=1000
for episode in range(episodes):
    state=env.reset()
    agent.reset()

    while True:
        action=agent.get_action(state)
        next_state,reward,done=env.step(action)
        agent.add(state,action,reward)
        if done :
            agent.eval()
            break
        state=next_state
show_val(agent.V)
    