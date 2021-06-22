from typing import Tuple

class State:
    def __init__(self):
        self.agent_x = 0
        self.agent_y = 5
        self.has_object = False
        self.object_x = 3
        self.object_y = 2

    def get_agent_position(self) -> Tuple[int, int]:
        return (self.agent_y, self.agent_x)

    def get_object_position(self) -> Tuple[int, int]:
        return (self.object_y, self.object_x)
