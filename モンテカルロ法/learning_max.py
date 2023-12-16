from grid import GridWorld
from max_agent import max_agent

env=GridWorld()
agent=max_agent()

episodes=100000

for episode in range(episodes):
    state= env.reset()
    agent.reset()

    while True :
        action = agent.get_action(state)
        next_state ,reward,done =env.step(action)
        agent.add(state,action,reward)
        if done:
            agent.update()
            break
        state=next_state
agent.show_Q(env)