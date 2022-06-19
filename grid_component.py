import numpy as np
import sys
import time
from parameters_component import ParametersComponent

np.set_printoptions(precision=4)
np.set_printoptions(threshold=sys.maxsize)  # display entire array


class GridComponent:
    Iteration = 0

    def __init__(self, file_name):
        self.Parameters = ParametersComponent()

        if not self.Parameters.load_parameters(file_name):
            exit(-1)

        if not self.initializeGridWorld():
            exit(-1)

    def initializeGridWorld(self):
        self.Utility = [
            [0 for c in range(self.Parameters.Col)] for r in range(self.Parameters.Row)
        ]
        self.Policy = [
            ["<" for c in range(self.Parameters.Col)]
            for r in range(self.Parameters.Row)
        ]

        for wall in self.Parameters.Walls:
            if wall[0] < self.Parameters.Row and wall[1] < self.Parameters.Col:
                self.Utility[wall[0]][wall[1]] = "X"
                self.Policy[wall[0]][wall[1]] = "X"
            else:
                print("Given wall is out of range of grid world", wall)
                return False

        for end_state in self.Parameters.EndStates:
            if (
                end_state[0] < self.Parameters.Row
                and end_state[1] < self.Parameters.Col
            ):
                if self.Utility[end_state[0]][end_state[1]] == "X":
                    print(
                        "Given end state cannot be placed where wall currently is.",
                        end_state,
                    )
                    return False

                self.Utility[end_state[0]][end_state[1]] = "[" + str(end_state[2]) + "]"
                self.Policy[end_state[0]][end_state[1]] = "E"
            else:
                print("Given end state is out of range of grid world", end_state)
                return False

        return True
