import numpy as np
from typing import List, Tuple

from model.grid_world import Action

class QAgent:
    def __init__(self, height: int, width: int, epsilon: float = 0.3, alpha: float = 0.1, gamma: float = 0.9):
        self.q_table = {}
        for x in range(width):
            for y in range(height):
                self.q_table[(y,x)] = {Action.UP:0, Action.DOWN:0, Action.RIGHT:0, Action.LEFT:0, Action.STAY:0} # Populate sub-dictionary with zero values for possible moves

        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def choose_action(self, actions: List[Action], agent_current_state: Tuple[int, int]) -> Action:
        if np.random.uniform(0,1) < self.epsilon:
            action = actions[np.random.randint(0, len(actions))]
        else:
            state_q_values = self.q_table[agent_current_state]
            maxValue = max(state_q_values.values())
            action = np.random.choice([k for k, v in state_q_values.items() if v == maxValue])
        
        return action
    
    def update_q_values(self, agent_current_state, reward, agent_new_state, action):
        new_state_q_values = self.q_table[agent_new_state]
        new_state_max_q_value = max(new_state_q_values.values())
        current_q_value = self.q_table[agent_current_state][action]
        
        self.q_table[agent_current_state][action] = current_q_value + self.alpha * (reward + self.gamma * new_state_max_q_value - current_q_value)