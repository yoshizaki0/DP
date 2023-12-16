from grid import GridWorld
from TD_agent import TD_agent

env=GridWorld()
agent=TD_agent()

episodes=1000

for episode in range(episodes):
    state=env.reset()

    while True :
        action = agent.get_action(state)
        next_state,reward,done = env.step(action)
        agent.eval(state,reward,next_state,done)
        if done :
            break
        state=next_state

agent.show(env)

