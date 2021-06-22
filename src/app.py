import json
from datetime import datetime

from model.q_agent import QAgent
from model.grid_world import GridWorld

MAX_STEPS_PER_EPISODE = 500
MAX_EPISODIES = 500

def main():
    steps_by_episode = []
    time_by_episode = []

    height = 6
    width = 7
    epsilon = 0.3
    alpha = 0.1
    gamma = 0.9
    q_agent = QAgent(height, width, epsilon=epsilon, alpha=alpha, gamma=gamma)
    
    episode = 0
    while episode < MAX_EPISODIES:
        grid_world = GridWorld(height, width)
        episode_init = datetime.now()
        steps = 0
        reach_goal_state = False
        while steps < MAX_STEPS_PER_EPISODE and not reach_goal_state:
            current_agent_state = grid_world.state.get_agent_position()
            action = q_agent.choose_action(grid_world.actions, current_agent_state) 
            reward = grid_world.make_step(action)
            new_agent_state = grid_world.state.get_agent_position()
            
            q_agent.update_q_values(current_agent_state, reward, new_agent_state, action)
                
            steps += 1
            
            reach_goal_state = grid_world.is_goal_state()

        episode_end = datetime.now()
        episode += 1

        steps_by_episode.append(steps)
        time_by_episode.append((episode_end - episode_init).microseconds)

    print(f"Passos por episódio: {steps_by_episode}")
    print(f"Tempo por episódio: {time_by_episode}")

    result_content = json.dumps({
            'epsilon': epsilon,
            'alpha': alpha,
            'gamma': gamma,
            'steps_by_episode': steps_by_episode,
            'time_by_episode': time_by_episode,
        })

    with open('result.txt', 'a') as file:
        file.write(f"{result_content}\n")

if __name__ == "__main__":
    main()