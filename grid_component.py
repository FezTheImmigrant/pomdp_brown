import numpy as np
import sys
import time
from parameters_component import ParametersComponent

np.set_printoptions(precision=4)
np.set_printoptions(threshold=sys.maxsize)  # display entire array


class GridComponent:
    iteration = 0

    def __init__(self, file_name):
        self.parameters = ParametersComponent()

        if not self.parameters.load_parameters(file_name):
            exit(-1)

        if not self.__initialize_grid():
            exit(-1)

    def __initialize_grid(self):
        """
        Create a utility and policy grid. Returns True if walls and end_states are valid parameters.

            Parameters:

            Returns:
                is_valid: (bool): Boolean of whether or not parameters are valid.
        """

        self.utility = [
            [0 for c in range(self.parameters.col)] for r in range(self.parameters.row)
        ]
        self.policy = [
            ["<" for c in range(self.parameters.col)]
            for r in range(self.parameters.row)
        ]

        return self.__initialize_walls() and self.__initialize_end_states()

    def __initialize_walls(self):
        """
        Initializes walls on utility and policy grid.
        Returns True if walls are in range of the grid world  row and column parameters.

            Parameters:

            Returns:
                is_valid: (bool): Boolean of whether or not walls are within the grid world parameters
        """

        for wall in self.parameters.walls:
            if wall[0] < self.parameters.row and wall[1] < self.parameters.col:
                self.utility[wall[0]][wall[1]] = "X"
                self.policy[wall[0]][wall[1]] = "X"
            else:
                print("Given wall is out of range of grid world", wall)
                return False

        return True

    def __initialize_end_states(self):
        """
        Initializes end states on utility and policy grid. 
        Returns True if end_states are in range of the grid world row and column parameters, and if there is not already a wall placed.

            Parameters:

            Returns:
                is_valid: (bool): Boolean of whether or not end states are within the grid world parameters
        """

        for end_state in self.parameters.end_states:
            if (
                end_state[0] < self.parameters.row
                and end_state[1] < self.parameters.col
            ):
                if self.utility[end_state[0]][end_state[1]] == "X":
                    print(
                        "Given end state cannot be placed where wall currently is.",
                        end_state,
                    )
                    return False

                self.utility[end_state[0]][end_state[1]] = "[" + str(end_state[2]) + "]"
                self.policy[end_state[0]][end_state[1]] = "E"
            else:
                print("Given end state is out of range of grid world", end_state)
                return False

        return True
