import numpy as np
from enum import Enum

from model.state import State

DEFAULT_REWARD = -0.5

class Action(Enum):
    UP = 'up'
    DOWN = 'down'
    RIGHT = 'right'
    LEFT = 'left'
    STAY = 'stay'

class GridWorld:
    def __init__(self, height: int, width: int):
        self.state = State()
        self.height = height
        self.width = width
        self.grid = np.zeros((self.height, self.width)) + DEFAULT_REWARD 
        self.walls = ((1, 3), (4, 0), (4, 1), (4, 3), (4, 4), (4, 5), (4, 6), (5, 6))
        self.base = ((0, 2), (0, 3), (0, 4))
        self.init_object_position = (2, 3)
        self.init_object_position_sides = ((2, 2), (2, 4))

        #Grid base rewards
        self.grid[self.base[0][0], self.base[0][1]] = 0
        self.grid[self.base[1][0], self.base[1][1]] = 0
        self.grid[self.base[2][0], self.base[2][1]] = 0

        self.actions = (Action.UP, Action.DOWN, Action.RIGHT, Action.LEFT, Action.STAY)
        
    def get_reward(self, object_taked: bool = False):
        if object_taked:
            return 0

        return self.grid[self.state.agent_y, self.state.agent_x]

    def make_step(self, action):
        if action == Action.UP:
            if self.state.agent_y == 0 \
                or (self.state.agent_y - 1, self.state.agent_x) in self.walls \
                or (self.state.has_object and (self.state.object_y - 1, self.state.object_x) in self.walls) \
                or (not self.state.has_object and (self.state.agent_y - 1, self.state.agent_x) == self.init_object_position):
                return self.get_reward()

            self.state.agent_y = self.state.agent_y - 1
            if self.state.has_object:
                self.state.object_y = self.state.object_y - 1
        
        if action == Action.DOWN:
            if self.state.agent_y == self.height - 1 \
                or (self.state.agent_y + 1, self.state.agent_x) in self.walls \
                or (self.state.has_object and (self.state.object_y + 1, self.state.object_x) in self.walls) \
                or (not self.state.has_object and (self.state.agent_y + 1, self.state.agent_x) == self.init_object_position):
                return self.get_reward()

            self.state.agent_y = self.state.agent_y + 1
            if self.state.has_object:
                self.state.object_y = self.state.object_y + 1

        if action == Action.RIGHT:
            # If agent is at the right, stay still, collect reward
            if self.state.agent_x == self.width - 1 \
                or (self.state.has_object and (self.state.object_x == self.width - 1)) \
                or (self.state.agent_y, self.state.agent_x + 1) in self.walls \
                or (self.state.has_object and (self.state.object_y, self.state.object_x + 1) in self.walls) \
                or (not self.state.has_object and (self.state.agent_y, self.state.agent_x + 1) == self.init_object_position):
                return self.get_reward()

            self.state.agent_x = self.state.agent_x + 1
            if self.state.has_object:
                self.state.object_x = self.state.object_x + 1

        if action == Action.LEFT:
            # If agent is at the left, stay still, collect reward
            if self.state.agent_x == 0 \
                or (self.state.has_object and (self.state.object_x == 0)) \
                or (self.state.agent_y, self.state.agent_x - 1) in self.walls \
                or (self.state.has_object and (self.state.object_y, self.state.object_x - 1) in self.walls) \
                or (not self.state.has_object and (self.state.agent_y, self.state.agent_x - 1) == self.init_object_position):
                return self.get_reward()

            self.state.agent_x = self.state.agent_x - 1
            if self.state.has_object:
                self.state.object_x = self.state.object_x - 1

        if action == Action.STAY:
            return self.get_reward()
        
        object_taked = self.state.get_agent_position() in self.init_object_position_sides and not self.state.has_object

        if object_taked:
            self.state.has_object = True

        return self.get_reward(object_taked)

    def is_goal_state(self) -> bool:
        return self.state.get_object_position() in self.base
